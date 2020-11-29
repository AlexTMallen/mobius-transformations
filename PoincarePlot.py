import pygame


class PoincarePlot:
    """A plotting tool that allows you to convert x and y coordinates to pixel values"""
    scale_to_pixels = None  # scaling factor
    yaxis = None  # float location of the vertical axis
    surf = None

    # input the range of x values (xmin, xmax) to display on the provided surface
    def __init__(self, surf, xmin, xmax):
        self.surf = surf
        self.scale_to_pixels = surf.get_width() / (xmax - xmin)
        self.yaxis = -xmin * self.scale_to_pixels

    def draw(self):
        self.surf.fill((0, 0, 0))
        self.draw_axes()

    def draw_axes(self):
        pygame.draw.line(self.surf, (255, 255, 255), (int(self.yaxis), 0), (int(self.yaxis), self.surf.get_height()), 2)
        pygame.draw.line(
            self.surf, (255, 255, 255),
            (0, self.surf.get_height()),
            (self.surf.get_width(), self.surf.get_height()),
            6
        )

    def convert_scale(self, s):
        return int(self.scale_to_pixels * s)

    def convertx(self, x):
        return int(self.yaxis + self.scale_to_pixels * x)

    def converty(self, y):
        return int(self.surf.get_height() - self.scale_to_pixels * y)

    def convert_point(self, p):
        return self.convertx(p[0]), self.converty(p[1])
