from random import sample
from numpy import zeros
import pygame

# Initialize pygame
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
fps = 30


# pattern for a baseline valid solution
def pattern(r, c, base, side):
    return (base * (r % base) + r // base + c) % side


# randomize rows, columns and numbers (of valid base pattern)
def shuffle(z):
    return sample(z, len(z))


def validate(sudoku, row, col):
    block_x = row // 3
    block_y = col // 3
    for k in range(9):
        if k != col and sudoku[row][k] == sudoku[row][col]:
            return False
        elif k != row and sudoku[k][col] == sudoku[row][col]:
            return False
    for a in range(3 * block_x, 3 * block_x + 3):
        for b in range(3 * block_y, 3 * block_y + 3):
            if a != row and b != col and sudoku[a][b] == sudoku[row][col]:
                return False
    return True


def solve_hidden(board_rand, row, col):
    while row < 9 and col < 9:
        if board_rand[row][col] == 0:
            for num in range(1, 10):
                board_rand[row][col] = num
                if validate(board_rand, row, col):
                    if col == 8 and row != 8:
                        if solve_hidden(board_rand, row + 1, 0):
                            return True
                        else:
                            board_rand[row][col] = 0
                    elif col == 8 and row == 8:
                        return True
                    else:
                        if solve_hidden(board_rand, row, col + 1):
                            return True
                        else:
                            board_rand[row][col] = 0
                else:
                    board_rand[row][col] = 0
            else:
                return False
        else:
            if col == 8 and row == 8:
                return True
            elif col == 8:
                row += 1
                col = 0
            else:
                col += 1


def generate_puzzle():
    base = 3
    side = base * base

    r_base = range(base)
    rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums = shuffle(range(1, base * base + 1))

    # produce board using randomized baseline pattern
    boxes = [[nums[pattern(r, c, base, side)] for c in cols] for r in rows]
    boxes_disposable = [[nums[pattern(r, c, base, side)] for c in cols] for r in rows]
    squares = side * side
    empties = squares * 3 // 4
    for p in sample(range(squares), empties):
        boxes[p // side][p % side] = 0
        boxes_disposable[p // side][p % side] = 0
    clock.tick(30)
    if solve_hidden(boxes_disposable, 0, 0):
        clock.tick(30)
        time = clock.get_time()
        if time > 50:
            return generate_puzzle()
        else:
            return boxes
    else:
        return generate_puzzle()


puzzle = generate_puzzle()
puzzle_disposable = puzzle.copy()
puzzle_const = puzzle_disposable.copy()
puzzle_temp = zeros((9, 9), int)

# Game Screen
screen = pygame.display.set_mode((623, 623))

# Title and Icon
pygame.display.set_caption('Sudoku')
icon = pygame.image.load('pastime.png')
pygame.display.set_icon(icon)

# Sudoku Display
font = pygame.font.SysFont('arial', 40)
font1 = pygame.font.SysFont('times', 30)
font2 = pygame.font.SysFont('arial', 20)


def board():
    for i in range(3):
        pygame.draw.line(screen, (0, 0, 0), (66 + i * 210, 0), (66 + i * 210, 623), 1)
        pygame.draw.line(screen, (0, 0, 0), (134 + i * 210, 0), (134 + i * 210, 623), 1)
        pygame.draw.line(screen, (0, 0, 0), (0, 66 + i * 210), (623, 66 + i * 210), 1)
        pygame.draw.line(screen, (0, 0, 0), (0, 134 + i * 210), (623, 134 + i * 210), 1)
    for i in range(2):
        pygame.draw.line(screen, (0, 0, 0), (202 + i * 210, 0), (202 + i * 210, 623), 7)
        pygame.draw.line(screen, (0, 0, 0), (0, 202 + i * 210), (623, 202 + i * 210), 7)
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                text = font.render(str(puzzle[i][j]), 1, (0, 0, 0))
                if i < 3:
                    if j < 3:
                        screen.blit(text, (j * 68 + 22, i * 68 + 10))
                    elif j < 6:
                        screen.blit(text, (j * 68 + 28, i * 68 + 10))
                    else:
                        screen.blit(text, (j * 68 + 34, i * 68 + 10))
                elif i < 6:
                    if j < 3:
                        screen.blit(text, (j * 68 + 22, i * 68 + 16))
                    elif j < 6:
                        screen.blit(text, (j * 68 + 28, i * 68 + 16))
                    else:
                        screen.blit(text, (j * 68 + 34, i * 68 + 16))
                else:
                    if j < 3:
                        screen.blit(text, (j * 68 + 22, i * 68 + 22))
                    elif j < 6:
                        screen.blit(text, (j * 68 + 28, i * 68 + 22))
                    else:
                        screen.blit(text, (j * 68 + 34, i * 68 + 22))
    for i in range(9):
        for j in range(9):
            if puzzle_temp[i][j] != 0 and puzzle[i][j] == 0:
                text = font2.render(str(puzzle_temp[i][j]), 1, (100, 100, 100))
                if i < 3:
                    if j < 3:
                        screen.blit(text, (j * 68 + 47, i * 68 + 5))
                    elif j < 6:
                        screen.blit(text, (j * 68 + 53, i * 68 + 5))
                    else:
                        screen.blit(text, (j * 68 + 59, i * 68 + 5))
                elif i < 6:
                    if j < 3:
                        screen.blit(text, (j * 68 + 47, i * 68 + 11))
                    elif j < 6:
                        screen.blit(text, (j * 68 + 53, i * 68 + 11))
                    else:
                        screen.blit(text, (j * 68 + 59, i * 68 + 11))
                else:
                    if j < 3:
                        screen.blit(text, (j * 68 + 47, i * 68 + 17))
                    elif j < 6:
                        screen.blit(text, (j * 68 + 53, i * 68 + 17))
                    else:
                        screen.blit(text, (j * 68 + 59, i * 68 + 17))


def solve(grid, row, col):
    while row < 9 and col < 9:
        if grid[row][col] == 0:
            pygame.event.pump()
            for num in range(1, 10):
                grid[row][col] = num
                screen.fill((255, 255, 255))
                board()
                draw_rect_bord(screen, row, col)
                pygame.display.update()
                if validate(grid, row, col):
                    if col == 8 and row != 8:
                        if solve(grid, row + 1, 0):
                            return True
                        else:
                            grid[row][col] = 0
                    elif col == 8 and row == 8:
                        return True
                    else:
                        if solve(grid, row, col + 1):
                            return True
                        else:
                            grid[row][col] = 0
                            screen.fill((255, 255, 255))
                            board()
                            draw_rect_bord(screen, row, col)
                            pygame.display.update()
                else:
                    grid[row][col] = 0
                    screen.fill((255, 255, 255))
                    board()
                    pygame.display.update()
            else:
                return False
        else:
            if col == 8 and row == 8:
                return True
            elif col == 8:
                row += 1
                col = 0
            else:
                col += 1


def get_rectangle(row, col):
    if row < 3:
        if col < 3:
            return 68 * col, 68 * row, 68, 68
        elif col < 6:
            return 68 * col + 5, 68 * row, 68, 68
        else:
            return 68 * col + 12, 68 * row, 68, 68
    elif row < 6:
        if col < 3:
            return 68 * col, 68 * row + 5, 68, 68
        elif col < 6:
            return 68 * col + 5, 68 * row + 5, 68, 68
        else:
            return 68 * col + 12, 68 * row + 5, 68, 68
    else:
        if col < 3:
            return 68 * col, 68 * row + 12, 68, 68
        elif col < 6:
            return 68 * col + 5, 68 * row + 12, 68, 68
        else:
            return 68 * col + 12, 68 * row + 12, 68, 68


def draw_rect_bord(surface, y, x, colour=(0, 255, 0)):
    rect_cords = get_rectangle(y, x)
    pygame.draw.rect(surface, (255, 255, 255), rect_cords, 0)
    for i in range(4):
        pygame.draw.rect(surface, colour, (rect_cords[0] - i, rect_cords[1] - i, 68, 68), 1)


def get_grid_cords(cords):
    dif = 623 / 9
    return int(cords[0] // dif), int(cords[1] // dif)


def check_input(bored, x, y, value):
    bored[x][y] = value
    pygame.event.pump()
    if not validate(bored, x, y):
        bored[x][y] = 0
        puzzle_temp[x][y] = 0
        screen.fill((255, 255, 255))
        draw_rect_bord(screen, x, y, (255, 0, 0))
        board()
        pygame.display.update()
        pygame.time.delay(500)
        return False
    elif not solve_hidden(bored, 0, 0):
        bored[x][y] = 0
        puzzle_temp[x][y] = 0
        screen.fill((255, 255, 255))
        draw_rect_bord(screen, x, y, (255, 0, 0))
        board()
        pygame.display.update()
        pygame.time.delay(500)
        return False
    else:
        puzzle[x][y] = value
        puzzle_temp[x][y] = 0
        return True


# Game loop
running = True
flag = 0
val = 0
delete = 0
confirm = 0
menu = 1
while running:
    # Background Colour
    screen.fill((255, 255, 255))
    if menu == 1:
        text_a = font.render("Sudoku", 2, (0, 0, 0))
        text_b = font1.render('Generate Puzzle', 1, (0, 0, 0))
        text_c = font1.render('Controls', 1, (0, 0, 0))
        text_d = font1.render('Quit Game', 1, (0, 0, 0))
        screen.blit(text_a, (250, 150))
        screen.blit(text_b, (200, 300))
        pygame.draw.rect(screen, (0, 0, 0), (190, 290, 250, 50), width=2)
        screen.blit(text_c, (250, 400))
        pygame.draw.rect(screen, (0, 0, 0), (230, 390, 150, 50), width=2)
        screen.blit(text_d, (240, 500))
        pygame.draw.rect(screen, (0, 0, 0), (230, 490, 150, 50), width=2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3)[0]:
                    button = pygame.mouse.get_pos()
                    if 190 <= button[0] <= 340:
                        if 290 <= button[1] <= 340:
                            menu = 0
                        if 390 <= button[1] <= 440:
                            menu = 2
                        if 490 <= button[1] <= 540:
                            running = False

        pygame.display.update()
    elif menu == 2:
        text_e = font.render("Controls", 2, (0, 0, 0))
        text_f = font1.render('Select a box by clicking on it.', 1, (0, 0, 0))
        text_g = font1.render('Pencil in a number by pressing the number', 1, (0, 0, 0))
        text_h = font1.render('button on a selected box.', 1, (0, 0, 0))
        text_k = font1.render('Confirm a penciled number by pressing enter.', 1, (0, 0, 0))
        text_i = font1.render('Press R to redo the puzzle and SPACE to solve it.', 1, (0, 0, 0))
        text_l = font1.render('Press N to generate a new puzzle.', 1, (0, 0, 0))
        text_m = font1.render('Press Esc to go back to Main menu.', 1, (0, 0, 0))
        text_j = font1.render('Back to Main Menu', 1, (0, 0, 0))
        screen.blit(text_e, (150, 50))
        screen.blit(text_f, (20, 150))
        screen.blit(text_g, (20, 210))
        screen.blit(text_h, (20, 260))
        screen.blit(text_k, (20, 320))
        screen.blit(text_i, (20, 380))
        screen.blit(text_l, (20, 440))
        screen.blit(text_m, (20, 470))
        screen.blit(text_j, (150, 520))
        pygame.draw.rect(screen, (0, 0, 0), (140, 510, 260, 50), width=2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3)[0]:
                    button = pygame.mouse.get_pos()
                    if 140 <= button[0] <= 400:
                        if 510 <= button[1] <= 560:
                            menu = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = 1
        pygame.display.update()
    elif menu == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve(puzzle, 0, 0)
                elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    val = 1
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    val = 2
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    val = 3
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    val = 4
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    val = 5
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    val = 6
                elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    val = 7
                elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    val = 8
                elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    val = 9
                elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    delete = 1
                elif event.key == pygame.K_RETURN:
                    confirm = 1
                elif event.key == pygame.K_r:
                    puzzle = puzzle_const.copy()
                elif event.key == pygame.K_n:
                    puzzle = generate_puzzle()
                    puzzle_disposable = puzzle.copy()
                    puzzle_const = puzzle_disposable.copy()
                    puzzle_temp = zeros((9, 9), int)
                elif event.key == pygame.K_ESCAPE:
                    menu = 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                grid_cords = get_grid_cords(pos)
                n = grid_cords[0]
                m = grid_cords[1]
                if puzzle[m][n] == 0:
                    flag = 1
                else:
                    flag = 2
        if flag == 1:
            # noinspection PyUnboundLocalVariable
            draw_rect_bord(screen, m, n)
        elif flag == 2:
            draw_rect_bord(screen, m, n, (0, 0, 255))
        if val != 0 and flag != 0:
            if puzzle[m][n] == 0:
                puzzle_temp[m][n] = val
            val = 0
        if delete == 1 and flag != 0 and puzzle_temp[m][n] != 0:
            puzzle_temp[m][n] = 0
            delete = 0
        if confirm == 1 and flag != 0 and puzzle_temp[m][n] != 0 and puzzle[m][n] == 0:
            check_input(puzzle_disposable, m, n, puzzle_temp[m][n])
            puzzle_disposable = puzzle.copy()
            confirm = 0
        board()
        pygame.display.update()
