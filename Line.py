import math
import pygame


class Line:
    """A hyperbolic geometry version of a line in the upper half-plane,
    which visually looks like a semicircle centered on the x axis
    (or in the limiting case a vertical ray)"""
    x1 = None
    x2 = None

    # x coordinates of the endpoints of the line
    def __init__(self, x1, x2):
        self.x1 = x1 if abs(x1) < 65536 else math.inf  # 2**16 is big enough to be considered infinite
        self.x2 = x2 if abs(x2) < 65536 else math.inf

    def center(self):
        return (self.x1 + self.x2) / 2

    def radius(self):
        return abs(self.x2 - self.x1) / 2

    # returns 'v' for vertical line, 's' for semicircle, or None if both endpoints are equal
    def type(self, plot):
        if math.isfinite(self.x1) and math.isfinite(self.x2):
            if plot.convert_scale(abs(self.x1 - self.x2)) <= 1:
                return None
            return 's'
        if math.isfinite(self.x1) or math.isfinite(self.x2):
            return 'v'
        return None

    def draw(self, color, plot, endpoints=False, lines=True):
        t = self.type(plot)
        if t == 'v':
            x = self.x1 if math.isfinite(self.x1) else self.x2
            if lines:
                pygame.draw.line(plot.surf, color, (plot.convertx(x), plot.xaxis), (plot.convertx(x), 0))
            if endpoints:
                pygame.draw.circle(plot.surf, color, plot.convert_point((x, plot.xaxis)), 5)
        elif t == 's':
            if lines:
                r = plot.convert_scale(self.radius())
                c = (plot.convertx(self.center()), plot.xaxis)
                pygame.draw.circle(
                    plot.surf,
                    color,
                    c,
                    r,
                    1
                )
            if endpoints:
                pygame.draw.circle(plot.surf, color, (plot.convertx(self.x1), plot.xaxis), 5)
                pygame.draw.circle(plot.surf, color, (plot.convertx(self.x2), plot.xaxis), 5)
        elif t is None:
            print("none")
