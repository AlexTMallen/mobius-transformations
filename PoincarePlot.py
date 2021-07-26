import pygame


class PoincarePlot:
    """A plotting tool that allows you to convert x and y coordinates to pixel values"""
    scale_to_pixels = None  # scaling factor
    yaxis = None  # float location of the vertical axis
    surf = None

    # input the range of x values (xmin, xmax) to display on the provided surface
    def __init__(self, surf, xmin, xmax, ymin):
        self.surf = surf
        self.scale_to_pixels = surf.get_width() / (xmax - xmin)
        self.yaxis = int(-xmin * self.scale_to_pixels)
        self.xaxis = int(surf.get_height() + ymin * self.scale_to_pixels)

    def draw(self, back_color):
        self.surf.fill(back_color)
        self.draw_axes()

    def hide_lower_half_plane(self, back_color):
        rect = pygame.Rect(0, self.xaxis + 4, self.surf.get_width(), self.surf.get_height())
        pygame.draw.rect(self.surf, back_color, rect)

    def draw_axes(self):
        pygame.draw.line(self.surf, (255, 255, 255), (self.yaxis, 0), (self.yaxis, self.surf.get_height()), 2)
        pygame.draw.line(
            self.surf, (255, 255, 255),
            (0, self.xaxis),
            (self.surf.get_width(), self.xaxis),
            6
        )

    def plot_point(self, point, color, size=5):
        if abs(point[0]) < 65536 and abs(point[1]) < 65536:
            pygame.draw.circle(self.surf, color, self.convert_point(point), size)

    def convert_scale(self, s):
        return int(self.scale_to_pixels * s)

    def convertx(self, x):
        return int(self.yaxis + self.scale_to_pixels * x)

    def converty(self, y):
        return int(self.xaxis - self.scale_to_pixels * y)

    def convert_point(self, p):
        return self.convertx(p[0]), self.converty(p[1])
