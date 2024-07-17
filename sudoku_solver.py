import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((540, 600))
pygame.display.set_caption("Sudoku Solver")

# Grid for the Sudoku puzzle
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def draw_grid():
    for i in range(0, 10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(screen, (0, 0, 0), (60 * i, 0), (60 * i, 540), thickness)
        pygame.draw.line(screen, (0, 0, 0), (0, 60 * i), (540, 60 * i), thickness)

def draw_numbers():
    font = pygame.font.SysFont(None, 40)
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                value = font.render(str(grid[i][j]), True, (0, 0, 0))
                screen.blit(value, (j * 60 + 20, i * 60 + 15))

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_valid(grid, num, pos):
    for i in range(9):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(9):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(grid, i, (row, col)):
            grid[row][col] = i
            draw_numbers()
            pygame.display.update()
            pygame.time.delay(50)

            if solve(grid):
                return True

            grid[row][col] = 0
            draw_numbers()
            pygame.display.update()
            pygame.time.delay(50)

    return False

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        draw_grid()
        draw_numbers()
        pygame.display.update()

        solve(grid)

        time.sleep(5)
        running = False

    pygame.quit()

if __name__ == "__main__":
    main()
