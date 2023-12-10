from dataclasses import dataclass

from domain.geometry import get_lines, is_on_line, scale_vertices
from domain.types import Point, Size, Trace

ALIGN_LEFT = 0
ALIGN_CENTER = 1
ALIGN_RIGHT = 2


class Glyph:
    glyph_vertices: list[Point]

    def __init__(self, glyph_vertices: list[Point]):
        self.glyph_vertices = glyph_vertices

    def trace(self, size: Size, stroke_width: float) -> Trace:
        (width, height) = size

        scaled_vertices = scale_vertices(self.glyph_vertices, (width, height))

        result: list[list[bool]] = [
            [False for _ in range(0, width)] for _ in range(0, height)
        ]

        lines = get_lines(scaled_vertices)

        for x in range(0, width):
            for y in range(0, height):
                p = (x, y)
                matches = [is_on_line(p, line, stroke_width) for line in lines]
                result[y][x] = any(matches)

        return result


@dataclass
class TextRendererOptions:
    width: int
    height: int
    glyph_height: int
    glyph_width_factor: float
    symbol: str
    font_dict: dict[str, list[Point]]
    color: str = ""
    alignment: int = ALIGN_LEFT
    stroke_width: float = 1
    gap: int = 1


@dataclass
class RenderParams:
    glyph_width: int
    glyph_height: int
    left_padding: int
    vert_padding: int


class TextRenderer:
    def __init__(self, options: TextRendererOptions):
        self.options = options

    def trace_glyphs(self, glyphs: list[Glyph], render_params: RenderParams) -> Trace:
        glyphs_len = len(glyphs)
        text_width = (
            glyphs_len * render_params.glyph_width + (glyphs_len - 1) * self.options.gap
        )
        text_height = render_params.glyph_height

        trace_result: Trace = [
            [False for _ in range(text_width)] for _ in range(text_height)
        ]

        for id, glyph in enumerate(glyphs):
            offset = id * render_params.glyph_width

            if id > 0:
                offset = offset + id * self.options.gap

            glyph_trace = glyph.trace(
                size=(render_params.glyph_width, render_params.glyph_height),
                stroke_width=self.options.stroke_width,
            )

            for y in range(render_params.glyph_height):
                for x in range(render_params.glyph_width):
                    trace_result[y][x + offset] = glyph_trace[y][x]

        return trace_result

    def render(self, text: str) -> str:
        if len(text) < 1 or len(self.options.symbol) < 1:
            return ""

        letters = list(self.options.font_dict.keys())
        text = text.lower()
        text_chars = list(text)

        text = "".join([(chr if chr in letters else "_") for chr in text_chars])

        text_chars = text.split()

        render_params = self.calculate_render_params(text_length=len(text))
        trace_result = self.trace_glyphs(
            glyphs=[Glyph(glyph_vertices=self.options.font_dict[chr]) for chr in text],
            render_params=render_params,
        )

        rendered_text = ""
        for row in trace_result:
            rendered_row = "".join(
                [(self.options.symbol[0] if is_match else " ") for is_match in row]
            )
            rendered_text += self.format_row(rendered_row, render_params) + "\n"

        return self.format_rendered_text(rendered_text.rstrip(), render_params)

    def calculate_render_params(self, text_length: int) -> RenderParams:
        glyph_width = int(self.options.glyph_height * self.options.glyph_width_factor)

        left_padding = 0
        vert_padding = 0

        if self.options.alignment == ALIGN_CENTER:
            left_padding = max(0, (self.options.width - glyph_width * text_length) // 2)
        elif self.options.alignment == ALIGN_RIGHT:
            left_padding = max(0, self.options.width - glyph_width)

        vert_padding = max(0, (self.options.height - self.options.glyph_height) // 2)

        return RenderParams(
            glyph_width=glyph_width,
            glyph_height=self.options.glyph_height,
            left_padding=left_padding,
            vert_padding=vert_padding,
        )

    def format_rendered_text(self, text: str, render_params: RenderParams) -> str:
        padding = "\n" * render_params.vert_padding
        return padding + text + padding

    def format_row(self, row: str, render_params: RenderParams) -> str:
        return " " * render_params.left_padding + row
