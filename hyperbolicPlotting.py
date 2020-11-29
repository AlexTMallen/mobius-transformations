import pygame
import math
import numpy as np
import scipy
from scipy.linalg import fractional_matrix_power

from PoincarePlot import PoincarePlot
from Line import Line


SQRT2 = 2**0.5


def f(x, k=1):
    # k - k/(x + 0i)
    if x == 0:
        return math.inf
    else:
        return k - k/x


def generate_endpoints(endpoints, current, min_size=0.2):
    if current.radius() > min_size:
        endpoints[0].append(current.x1)
        endpoints[0].append(current.x2)
        endpoints[1].append(1)
        endpoints[1].append(1)
        center = current.center()
        left = center - current.radius() * SQRT2
        right = center + current.radius() * SQRT2
        generate_endpoints(endpoints, Line(left, center), min_size=min_size)
        generate_endpoints(endpoints, Line(center, right), min_size=min_size)


def main():
    # PLAY AROUND WITH THESE
    w = pygame.display.set_mode((600, 300))
    plot = PoincarePlot(w, -5, 5)
    min_size = 1
    initial_line = Line(-10, 10)
    endpoints = [[], []]
    generate_endpoints(endpoints, initial_line, min_size=min_size)
    endpoints = np.array(endpoints)
    k = 1
    step = 0.01
    transition = scipy.linalg.fractional_matrix_power(np.array([[k, -k],
                           [1,  0]], dtype=complex), step)

    num_iters = 0
    running = True
    while running:
        # event loop
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False

        # drawing
        plot.draw()
        for i in range(0, len(endpoints[0]), 2):
            line = Line(endpoints[0,i] / endpoints[1,i], endpoints[0,i+1] / endpoints[1,i+1])
            line.draw((255, 0, 0), plot)
        plot.draw_axes()

        endpoints = transition @ endpoints

        pygame.display.flip()
        if num_iters * step % 1 == 0:
            pygame.time.wait(1200)
        pygame.time.wait(20)
        num_iters += 1


if __name__ == "__main__":
    main()
