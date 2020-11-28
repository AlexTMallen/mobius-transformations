import pygame
import math

from PoincarePlot import PoincarePlot
from Line import Line


def main():
    # PLAY AROUND WITH THESE
    w = pygame.display.set_mode((600, 300))
    plot = PoincarePlot(w, -5, 5)
    lines = [Line(i, 0) for i in range(-9, 10)]

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
        pygame.display.flip()
        pygame.time.wait(100)


if __name__ == "__main__":
    main()
