import pygame
import math
import numpy as np
import scipy
from scipy.linalg import fractional_matrix_power
import time

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
    w = pygame.display.set_mode((1200, 700))
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
    k = 2  # 1 + (1 + np.sqrt(5)) / 2
    n_steps = 40
    trans = np.array([[0, 1],
                      [1,  0]], dtype=complex)
    transition = scipy.linalg.fractional_matrix_power(trans, 1 / n_steps)
    # trans1 = np.array([[1.5, 0],
    #                    [0, 1]], dtype=complex)
    # transition1 = scipy.linalg.fractional_matrix_power(trans1, 1 / n_steps)
    # trans2 = np.array([[1, 2],
    #                    [0, 1]], dtype=complex)
    # transition2 = scipy.linalg.fractional_matrix_power(trans2, 1 / n_steps)
    started_blue_dot = False

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
        # line = Line(-1, 1)
        # line.draw((100, 100, 100), plot, endpoints=True, lines=True)

        idx = upper
        if started_blue_dot:  # second
            plot.plot_point((endpoints[0, idx] / endpoints[1, idx], 0), color=blue, size=5)
        # fixed point is (0.5, np.sqrt(3) / 2) for k=1, (1, 1) for k=2, (1.33, 0.925) for k=1+phi
        # plot.plot_point((1, 1), color=(0, 0, 0), size=5)
        # line = Line(endpoints[0, upper - 1] / endpoints[1, upper - 1], endpoints[0, upper + 1] / endpoints[1, upper + 1])
        # line.draw(blue, plot, endpoints=True, lines=True)

        plot.hide_lower_half_plane(back_color)
        pygame.display.flip()

        # if num_iters % n_steps == 0:
            # if num_iters == (4 * n_steps):
            #     pygame.time.wait(2000)
            #     print("STARTED")
            #     plot.plot_point((endpoints[0, idx] / endpoints[1, idx], 0), color=blue, size=5)
            #     pygame.display.flip()
            #     started_blue_dot = True
            #     pygame.time.wait(500)
            # else:
            #    pygame.time.wait(00)
            # pygame.time.wait(500)

        mercy_delay = 100  # iterations
        # if mercy_delay < num_iters < n_steps + mercy_delay:
        #     endpoints = transition1 @ endpoints
        # elif num_iters == n_steps + mercy_delay:
        #     pygame.time.wait(2000)
        # elif mercy_delay < num_iters < 2 * n_steps + mercy_delay:
        #     endpoints = transition2 @ endpoints
        # else:
        #     pygame.time.wait(10)
        if mercy_delay < num_iters < n_steps + mercy_delay:
            endpoints = transition @ endpoints
        pygame.time.wait(40)
        num_iters += 1


if __name__ == "__main__":
    main()
