import pygame
import numpy as np

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_SIZE = 800
CELL_SIZE = 20
MARGIN = 3
NUM_CELLS = int(SCREEN_SIZE/CELL_SIZE)+2*MARGIN
NCOL_CELLS = int(SCREEN_WIDTH/CELL_SIZE)+2*MARGIN
NROW_CELLS = int(SCREEN_HEIGHT/CELL_SIZE)+2*MARGIN
CELL_BORDER = 1
FPS = 10
BACKGROUND_MUSIC = pygame.mixer.Sound('media/background1.wav')

data = np.random.randint(2, size = (NROW_CELLS, NCOL_CELLS))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Cellular automaton (Version 1 - Purple Chaos)')

def cell_state(i, j):
    x = int(np.sqrt(data[i,j]**2+2))
    return((x%50, x%150, x%150))

def update_states():
    for i in range(1,NROW_CELLS - 1):
        for j in range(1, NCOL_CELLS - 1):
            sum = data[i-1, j] + data[i, i-1] + data[i, j+1] + data[i+1, j] + data[i+1, j+1]
            #sum = data[i-1, j-1] + data[i-1, j] + data[i-1, j+1] + data[i, i-1] + data[i, j+1] + data[i+1, j-1] + data[i+1, j] + data[i+1, j+1]
            if sum > 100:
                data[i, j] -= 1
            else:
                data[i, j] += 1

def draw_cells():
    screen.fill((0, 0, 0))
    for i in range(1, NROW_CELLS - 1):
        for j in range(1, NCOL_CELLS - 1):
            cell = pygame.Rect(j*CELL_SIZE-MARGIN*CELL_SIZE, i*CELL_SIZE-MARGIN*CELL_SIZE, CELL_SIZE-CELL_BORDER, CELL_SIZE-CELL_BORDER)
            pygame.draw.rect(screen, cell_state(i, j), cell)

    pygame.display.update()
    #generation += 1


def main():
    #generation = 1
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.mixer.Sound.play(BACKGROUND_MUSIC)
        pygame.mixer.music.stop()
        update_states()
        draw_cells()

    pygame.quit()

if __name__ == "__main__":
    main()
