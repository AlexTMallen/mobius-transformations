import pygame


def main():
    win = pygame.display.set_mode((500, 500))
    w = 120
    h = 100
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255), (255, 255, 0), (255, 0, 255)]
    rects = []

    k = 3
    rt_k = k**0.5

    i = 0
    running = True
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False

        win.fill((255, 255, 255))
        rects.append((pygame.Rect((200, 200), (w, h)), colors[i % len(colors)]))
        w, h = int(rt_k*w - rt_k*h), int(w / rt_k)
        for rect, color in rects[::1]:
            pygame.draw.rect(win, color, rect)

        pygame.time.wait(600)
        pygame.display.flip()
        i += 1

if __name__ == "__main__":
    main()