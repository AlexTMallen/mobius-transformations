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
    w = pygame.display.set_mode((800, 500))
    back_color = (200, 200, 200)
    line_color = (200, 50, 50)
    blue = (100, 100, 200)
    plot = PoincarePlot(w, -5, 5, -1)
    # min_size = 1
    # initial_line = Line(-10, 10)
    # endpoints = [[], []]
    # generate_endpoints(endpoints, initial_line, min_size=min_size)
    lower, upper = -10, 10
    endpoints = [list(range(lower, upper)), [1] * (upper - lower)]
    # endpoints = [[-20], [-5]]
    endpoints = np.array(endpoints)
    k = 1
    step = 0.02
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
        plot.draw(back_color)
        for int_step in [2, 4, 8, 12]:
            for i in range(0, len(endpoints[0]) - int_step):
                line = Line(endpoints[0, i] / endpoints[1, i], endpoints[0, i + int_step] / endpoints[1, i + int_step])
                line.draw(line_color, plot, endpoints=True, lines=True)
        line = Line(-1, 1)
        line.draw((100, 100, 100), plot, endpoints=True, lines=True)

        idx = upper
        # plot.plot_point((endpoints[0, idx] / endpoints[1, idx], 0), color=blue)
        plot.plot_point((0.5, np.sqrt(3) / 2), color=(0,0,0), size=5)
        line = Line(endpoints[0, upper - 1] / endpoints[1, upper - 1], endpoints[0, upper + 1] / endpoints[1, upper + 1])
        line.draw(blue, plot, endpoints=True, lines=True)

        plot.hide_lower_half_plane(back_color)
        pygame.display.flip()

        endpoints = transition @ endpoints

        if num_iters * step % 1 == 0:
            pygame.time.wait(0)
        pygame.time.wait(40)
        num_iters += 1


if __name__ == "__main__":
    main()
