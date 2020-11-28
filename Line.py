import math
import pygame


class Line:
    """A hyperbolic geometry version of a line in the upper half-plane,
    which visually looks like a semicircle centered on the x axis in
    (or in the limiting case a vertical ray)"""
    x1 = None
    x2 = None

    def __init__(self, x1, x2):
        self.x1, self.x2 = x1, x2

    def center(self):
        return (self.x1 + self.x2) / 2

    def radius(self):
        return abs(self.x2 - self.x1) / 2

    # returns 'v' for vertical line, 's' for semicircle, or None if both endpoints are equal
    def type(self):
        if math.isfinite(self.x1) and math.isfinite(self.x2):
            if self.x1 == self.x2:
                return None
            return 's'
        if math.isfinite(self.x1) or math.isfinite(self.x2):
            return 'v'
        return None

    def draw(self, color, plot):
        t = self.type()
        if t == 'v':
            x = self.x1 if math.isfinite(self.x1) else self.x2
            pygame.draw.line(plot.surf, color, plot.convert_point(x, 0), plot.convert_point(x, plot.surf.get_height()))
        elif t == 's':
            pygame.draw.circle(
                plot.surf,
                color,
                plot.convert_point((self.center(), 0)),
                plot.convert_scale(self.radius()),
                1
            )
