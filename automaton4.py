import pygame
import numpy as np

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

FPS = 30
COLORS = {"TREE": (19, 136, 8), "FIRE": (240, 60, 20), "EMPTY": (20, 20, 0)}

p_tree = 0.1 #probability of filling empty cell with a tree
p_ignit = 0.0005 #probability of spontaneous ignition

MARGIN = 1
CELL_SIZE = 15
NCOL_CELLS = int(SCREEN_WIDTH/CELL_SIZE) + 2*MARGIN
NROW_CELLS = int(SCREEN_HEIGHT/CELL_SIZE) + 2*MARGIN
CELL_BORDER = 0

def calculate_future(screen, data):
    future = data.copy()
    for i in range(1, NROW_CELLS - 1):
        for j in range(1, NCOL_CELLS - 1):
            neighbors = [data[i-1, j-1], data[i-1, j], data[i-1, j+1], data[i+1, j-1], data[i+1, j], data[i+1, j+1], data[i, j-1], data[i, j+1]]
            state_color = COLORS[data[i, j]]
            cell = (j*CELL_SIZE - MARGIN*CELL_SIZE, i*CELL_SIZE - MARGIN*CELL_SIZE, CELL_SIZE - CELL_BORDER, CELL_SIZE - CELL_BORDER)
            pygame.draw.rect(screen, state_color, cell)

            if data[i, j] == "EMPTY":
                future[i, j] = np.random.choice(["TREE", "EMPTY"], 1, p = [p_tree, 1 - p_tree])[0]
            elif data[i, j] == "TREE":
                future[i, j] = "FIRE" if "FIRE" in neighbors else np.random.choice(["TREE", "FIRE"], 1, p = [1 - p_ignit, p_ignit])[0]
            elif data[i, j] == "FIRE":
                future[i, j] = "EMPTY"
            else:
                future[i, j] = "TREE"

    return future

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Cellular automaton (Version 4 - Forest-fire)")
    clock = pygame.time.Clock()

    data = np.array(NROW_CELLS*NCOL_CELLS*["EMPTY"]).reshape([NROW_CELLS, NCOL_CELLS])
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill(COLORS["EMPTY"])
        data = calculate_future(screen, data)
        pygame.display.update()

if __name__ == "__main__":
    main()
