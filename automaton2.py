import pygame
import numpy as np

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

FPS = 10
DEAD = (0, 9, 26)
ALIVE = (22, 73, 121)

CELL_SIZE = 30
MARGIN = 10
NCOL_CELLS = int(SCREEN_WIDTH/CELL_SIZE)+2*MARGIN
NROW_CELLS = int(SCREEN_HEIGHT/CELL_SIZE)+2*MARGIN
CELL_BORDER = 1
LIVING_CELLS_PROPORTION = 0.3

def calculate_future(screen, data):
    future = np.zeros([NROW_CELLS, NCOL_CELLS])
    for i in range(1, NROW_CELLS - 1):
        for j in range(1, NCOL_CELLS - 1):
            sum = np.sum(data[i-1:i+2, j-1:j+2]) - data[i, j]
            if (data[i, j] == 1 and 2 <= sum <= 3) or (data[i, j] == 0 and sum == 3):
                future[i, j] = 1
            state_color = ALIVE if future[i, j] == 1 else DEAD
            cell = (j*CELL_SIZE - MARGIN*CELL_SIZE, i*CELL_SIZE - MARGIN*CELL_SIZE, CELL_SIZE - CELL_BORDER, CELL_SIZE - CELL_BORDER)
            pygame.draw.rect(screen, state_color, cell)
    return future

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Cellular automaton (Version 2 - Game of Life)')
    clock = pygame.time.Clock()

    data = np.random.choice(2, NROW_CELLS*NCOL_CELLS, p = [1 - LIVING_CELLS_PROPORTION, LIVING_CELLS_PROPORTION]).reshape([NROW_CELLS, NCOL_CELLS])

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill(DEAD)
        data = calculate_future(screen, data)
        pygame.display.update()

if __name__ == "__main__":
    main()
