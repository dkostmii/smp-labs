from lab4.domain.types import Point, Trace, Size, SizeF, Line
from math import sqrt
from std.math import map, get_window


# Assume points are [0, width] and [0, height]
def map_point(point: Point,
              width_input: float, height_input: float,
              width_output: float, height_output: float) -> Point:
    return (
            map(point[0], 0, width_input, 0, width_output - 1),
            map(point[1], 0, height_input, 0, height_output - 1),
        )

def calc_offset(stroke_width: float) -> float:
    return stroke_width * sqrt(2) / 2


def get_dist_to_line(line: Line, p: Point) -> float:
    (p1, p2) = line
    (x1, y1) = p1
    (x2, y2) = p2

    (xp, yp) = p

    numerator = abs((x2 - x1) * (y1 - yp) - (x1 - xp) * (y2 - y1))
    denominator = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return numerator / denominator


def is_on_line(point: Point, line: Line, stroke_width: float):
    (p1, p2) = line
    (x1, y1) = p1
    (x2, y2) = p2

    if x1 > x2:
        (x1, x2) = (x2, x1)

    if y1 > y2:
        (y1, y2) = (y2, y1)

    (xp, yp) = point

    stroke_radius = calc_offset(stroke_width / 2) if stroke_width > 0.25 else 0.25
    dist = get_dist_to_line(line, point)

    result = (
        dist <= stroke_radius
        and xp >= x1 - stroke_radius and xp <= x2 + stroke_radius
        and yp >= y1 - stroke_radius and yp <= y2 + stroke_radius
    )

    return result


def scale_vertices(glyph_vertices: list[Point], size: SizeF) -> list[Point]:
    (width, height) = size

    return [map_point(p, 1, 1, width, height) for p in glyph_vertices]


def get_lines(vertices: list[Point]) -> list[Line]:
    return [
        tuple(get_window(2, offset, vertices))
        for offset in range(len(vertices) - 1)
    ]
