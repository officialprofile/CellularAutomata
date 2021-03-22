import pygame
import numpy as np

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
CELL_SIZE = 20
MARGIN = 3
NCOL_CELLS = int(SCREEN_WIDTH/CELL_SIZE)+2*MARGIN
NROW_CELLS = int(SCREEN_HEIGHT/CELL_SIZE)+2*MARGIN
CELL_BORDER = 0
FPS = 10

def update_states(data):
    new_generation = np.zeros([NROW_CELLS, NCOL_CELLS])
    for i in range(2,NROW_CELLS - 2):
        for j in range(2, NCOL_CELLS - 2):
            sum = (np.sum(data[i-2:i+3, j-2:j+3]) - data[i, j]) + (np.sum(data[i-1:i+2, j-1:j+2]) - data[i, j])
            if 0 < sum < 40:
                new_generation[i, j] = data[i, j] + 2
            elif data[i, j] > 10 and sum >= 40:
                new_generation[i, j] = data[i, j] - 1
            else:
                new_generation[i, j] = 0
    return new_generation


def draw_cells(screen, data):
    for i in range(2, NROW_CELLS - 2):
        for j in range(2, NCOL_CELLS - 2):
            cell_color = (int(data[i, j])+50, int(data[i, j]), int(data[i, j])+70)
            cell = pygame.Rect(j*CELL_SIZE-MARGIN*CELL_SIZE, i*CELL_SIZE-MARGIN*CELL_SIZE, CELL_SIZE-CELL_BORDER, CELL_SIZE-CELL_BORDER)
            pygame.draw.rect(screen, cell_color, cell)


def main():
    pygame.init()
    BACKGROUND_MUSIC = pygame.mixer.Sound('media/background1.wav')
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Cellular automaton (Version 1 - Purple Chaos)')
    clock = pygame.time.Clock()

    data = np.random.randint(2, size = (NROW_CELLS, NCOL_CELLS))

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        pygame.mixer.Sound.play(BACKGROUND_MUSIC)
        pygame.mixer.music.stop()
        draw_cells(screen, data)
        data = update_states(data)
        pygame.display.update()

if __name__ == "__main__":
    main()
