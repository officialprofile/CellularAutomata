import pygame
import numpy as np

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

FPS = 30
OFF = (10, 9, 16)
ON = (90, 43, 51)
CURRENT = (200, 20, 20)

CELL_SIZE = 15
NCOL_CELLS = int(SCREEN_WIDTH/CELL_SIZE)
NROW_CELLS = int(SCREEN_HEIGHT/CELL_SIZE)
CELL_BORDER = 0

def calculate_future(screen, data, x, y):
    future = data.copy()
    for i in range(NROW_CELLS):
        for j in range(NCOL_CELLS):
            state_color = CURRENT if (i, j) == (x, y) else ON if future[i, j] else OFF
            cell = (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE - CELL_BORDER, CELL_SIZE - CELL_BORDER)
            pygame.draw.rect(screen, state_color, cell)

    x += np.random.choice([-1, 0, 1], 1)
    y += np.random.choice([-1, 0, 1], 1)
    # border conditions
    if x < 0:
        x += 1
    if y < 0:
        y += 1
    if x == NROW_CELLS:
        x -= 1
    if y == NCOL_CELLS:
        y -= 1
    # not sure why this doesn't work
    # x = x + 1 if x < 0 else x - 1 if x >= NROW_CELLS - 1 else x
    # y = y + 1 if y < 0 else y - 1 if y >= NCOL_CELLS - 1 else y

    if data[x, y] == 0:
        future[x, y] = 1
    else:
        future[x, y] = 0
    return future

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Cellular automaton (Version 3 - Langton's Ant)")
    clock = pygame.time.Clock()

    data = np.zeros([NROW_CELLS, NCOL_CELLS])
    x, y = np.random.choice(NROW_CELLS, 1), np.random.choice(NCOL_CELLS, 1)
    data[x, y] = 1

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill(OFF)
        data = calculate_future(screen, data, x, y)
        pygame.display.update()

if __name__ == "__main__":
    main()
