import pygame
import numpy as np

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
CELL_SIZE = 10
MARGIN = 10
NCOL_CELLS = int(SCREEN_WIDTH/CELL_SIZE)+2*MARGIN
NROW_CELLS = int(SCREEN_HEIGHT/CELL_SIZE)+2*MARGIN
CELL_BORDER = 0
FPS = 20
ALIVE = (70, 150, 150)
DEAD = (10, 5, 40)
COLORS = [DEAD, ALIVE]

data = np.random.randint(2, size = (NROW_CELLS, NCOL_CELLS))
data_new = data

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Cellular automaton (Version 2 - Game of Life)')

def cell_state(i, j):
    sum = data[i-1, j-1] + data[i-1, j] + data[i-1, j+1] + data[i, i-1] + data[i, j+1] + data[i+1, j-1] + data[i+1, j] + data[i+1, j+1]
    if data[i, j] == 0 and sum == 3:
        return(1)
    if data[i, j] == 1 and (sum < 2 or sum > 3):
        return(0)
    else:
        return(data[i, j])

def update_states():
    for i in range(1, NROW_CELLS - 1):
        for j in range(1, NCOL_CELLS - 1):
            data_new[i, j] = cell_state(i, j)

def draw_cells():
    screen.fill((0, 0, 0))
    for i in range(1, NROW_CELLS - 1):
        for j in range(1, NCOL_CELLS - 1):
            cell = pygame.Rect(j*CELL_SIZE-MARGIN*CELL_SIZE, i*CELL_SIZE-MARGIN*CELL_SIZE, CELL_SIZE-CELL_BORDER, CELL_SIZE-CELL_BORDER)
            pygame.draw.rect(screen, COLORS[data_new[i, j]], cell)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        update_states()
        draw_cells()
        data = data_new

    pygame.quit()

if __name__ == "__main__":
    main()
