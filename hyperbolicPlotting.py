import pygame
import math

from PoincarePlot import PoincarePlot
from Line import Line


SQRT2 = 2**0.5


def f(x, k=1):
    # k - k/(x + 0i)
    if x == 0:
        return math.inf
    else:
        return k - k/x

def generate_lines(lines, current, min_size=0.2):
    if current.radius() > min_size:
        lines.append(current)
        center = current.center()
        left = center - current.radius() * SQRT2
        right = center + current.radius() * SQRT2
        generate_lines(lines, Line(left, center), min_size=min_size)
        generate_lines(lines, Line(center, right), min_size=min_size)


def main():
    # PLAY AROUND WITH THESE
    w = pygame.display.set_mode((600, 300))
    plot = PoincarePlot(w, -5, 5)
    lines = [Line(-10, 10)]
    generate_lines(lines, lines[0], min_size=0.4)

    running = True
    while running:
        # event loop
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False

        # drawing
        plot.draw()
        for line in lines:
            line.draw((255, 0, 0), plot)
            line.x1 = f(line.x1)
            line.x2 = f(line.x2)
        plot.draw_axes()
        pygame.display.flip()
        pygame.time.wait(5000)


if __name__ == "__main__":
    main()
