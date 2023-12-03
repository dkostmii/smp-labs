from dataclasses import dataclass
from math import cos, sin

from lab5.domain.geometry import get_line_length, get_lines, is_on_line, scale_vertices
from lab5.domain.types import Angle3F, Point, Point3F, Size, Trace
from std.math import sign

ALIGN_LEFT = 0
ALIGN_CENTER = 1
ALIGN_RIGHT = 2


class InvalidObjectTypeException(Exception):
    def __init__(self, object_type: str):
        super().__init__(self, f"Invalid object type: {object_type}")


@dataclass
class ProjectionParams:
    """Represents parameters used to project an object onto 2D project_onto_plane

    Attributes:
    c     Camera position
    theta Camera rotation
    e     Display surface (plane, onto which image is projected) position relative
          to the camera pinhole
    """

    c: Point3F
    theta: Angle3F
    e: Point3F


def project_point(point: Point3F, params: ProjectionParams) -> Point:
    a = point
    c = params.c
    theta = params.theta
    e = params.e

    cx, cy, cz = (cos(theta[0]), cos(theta[1]), cos(theta[2]))
    sx, sy, sz = (sin(theta[0]), sin(theta[1]), sin(theta[2]))

    x, y, z = (a[0] - c[0], a[1] - c[1], a[2] - c[2])

    dx = cy * (sz * y + cz * x) - sy * z
    dy = sx * (cy * z + sy * (sz * y + cz * x)) + cx * (cz * y - sz * x)
    dz = cx * (cy * z + sy * (sz * y + cz * x)) - sx * (cz * y - sz * x)

    ex, ey, ez = e

    # bx = ez / dz * dx + ex
    # by = ez / dz * dy + ey
    bx = (dx - ex) * (ez / dz if dz != 0 else sign(ez))
    by = (dy - ey) * (ez / dz if dz != 0 else sign(ez))

    return (bx, by)


def project_onto_plane(
    vertices: list[Point3F], params: ProjectionParams
) -> list[Point]:
    return [project_point(point, params) for point in vertices]


class RenderObject:
    object_vertices: list[Point3F]

    def __init__(self, object_vertices: list[Point3F]):
        self.object_vertices = object_vertices

    def trace(
        self, size: Size, stroke_width: float, projection_params: ProjectionParams
    ) -> Trace:
        (width, height) = size

        projected_vertices = project_onto_plane(
            vertices=self.object_vertices, params=projection_params
        )

        scaled_vertices = scale_vertices(projected_vertices, (width, height))
        lines = list(
            filter(lambda line: get_line_length(line) > 0, get_lines(scaled_vertices))
        )

        result: list[list[bool]] = [
            [False for _ in range(width)] for _ in range(height)
        ]

        for y in range(height):
            for x in range(width):
                p = (x, y)
                matches = [is_on_line(p, line, stroke_width) for line in lines]
                result[y][x] = any(matches)

        return result


@dataclass
class ObjectRendererOptions:
    width: int
    height: int
    object_height: int
    object_width: int
    symbol: str
    object_dict: dict[str, list[Point3F]]
    projection_params: ProjectionParams
    color: str = ""
    alignment: int = ALIGN_LEFT
    stroke_width: float = 1


@dataclass
class RenderParams:
    object_width: int
    object_height: int
    left_padding: int
    vert_padding: int


class ObjectRenderer:
    def __init__(self, options: ObjectRendererOptions):
        self.options = options

    def trace_object(
        self,
        render_object: RenderObject,
        render_params: RenderParams,
        projection_params: ProjectionParams,
    ) -> Trace:
        trace_result: Trace = [
            [False for _ in range(render_params.object_width)]
            for _ in range(render_params.object_height)
        ]

        object_trace = render_object.trace(
            size=(render_params.object_width, render_params.object_height),
            stroke_width=self.options.stroke_width,
            projection_params=projection_params,
        )

        for y in range(render_params.object_height):
            for x in range(render_params.object_width):
                trace_result[y][x] = object_trace[y][x]

        return trace_result

    def render(self, object_type: str) -> str:
        if object_type not in self.options.object_dict.keys():
            raise InvalidObjectTypeException(object_type)

        render_params = self.calculate_render_params()

        object_vertices = self.options.object_dict[object_type]

        trace_result = self.trace_object(
            render_object=RenderObject(object_vertices=object_vertices),
            render_params=render_params,
            projection_params=self.options.projection_params,
        )

        rendered_text = ""
        for row in trace_result:
            rendered_row = "".join(
                [(self.options.symbol[0] if is_match else " ") for is_match in row]
            )
            rendered_text += self.format_row(rendered_row, render_params) + "\n"

        return self.format_rendered_text(rendered_text.rstrip(), render_params)

    def calculate_render_params(self) -> RenderParams:
        left_padding = 0
        vert_padding = 0

        if self.options.alignment == ALIGN_CENTER:
            left_padding = max(0, (self.options.width - self.options.object_width) // 2)
        elif self.options.alignment == ALIGN_RIGHT:
            left_padding = max(0, self.options.width - self.options.object_width)

        vert_padding = max(0, (self.options.height - self.options.object_height) // 2)

        return RenderParams(
            object_width=self.options.object_width,
            object_height=self.options.object_height,
            left_padding=left_padding,
            vert_padding=vert_padding,
        )

    def format_rendered_text(self, text: str, render_params: RenderParams) -> str:
        padding = "\n" * render_params.vert_padding
        return padding + text + padding

    def format_row(self, row: str, render_params: RenderParams) -> str:
        return " " * render_params.left_padding + row
