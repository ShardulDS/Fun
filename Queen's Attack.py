def column_maker(matrix, index):
    col = []
    for i in matrix:
        col.append(i[index])
    return col


def queensAttack(n, k, r_q, c_q, obstacles, column):
    zeros = [0]*n
    board = []
    for _ in range(n):
        board.append(zeros.copy())
    board[r_q - 1][c_q - 1] += 2
    for i in obstacles:
        board[i[0]-1][i[1]-1] += 1
    left = 0
    right = 0
    up = 0
    down = 0
    up_right = 0
    up_left = 0
    down_right = 0
    down_left = 0
    obstacles_yet = 0
    if 1 in board[r_q-1]:
        obstacles_yet += board[r_q - 1].count(1)
        for p in reversed(range(c_q - 1)):
            if board[r_q - 1][p] == 1:
                break
            left += 1
        for j in range(c_q, n):
            if board[r_q - 1][j] == 1:
                break
            right += 1
    else:
        right += n - c_q
        left += c_q - 1
    if 1 in column(board, c_q - 1):
        obstacles_yet += column(board, c_q - 1).count(1)
        for z in reversed(range(r_q - 1)):
            if board[z][c_q - 1] == 1:
                break
            up += 1
        for j in range(r_q, n):
            if board[j][c_q - 1] == 1:
                break
            down += 1
    else:
        down += n - r_q
        up += r_q - 1
    if obstacles_yet < k:
        row = r_q - 1
        column = c_q - 1
        while row > 0 and column < n - 1:
            row -= 1
            column += 1
            if board[row][column] == 1:
                break
            else:
                up_right += 1
        row = r_q - 1
        column = c_q - 1
        while row > 0 and column > 0:
            row -= 1
            column -= 1
            if board[row][column] == 1:
                break
            else:
                up_left += 1
        row = r_q - 1
        column = c_q - 1
        while row < n - 1 and column < n - 1:
            row += 1
            column += 1
            if board[row][column] == 1:
                break
            else:
                down_right += 1
        row = r_q - 1
        column = c_q - 1
        while row < n - 1 and column > 0:
            row += 1
            column -= 1
            if board[row][column] == 1:
                break
            else:
                down_left += 1
    else:
        up_right += min([r_q - 1, n - c_q])
        up_left += min([r_q - 1, c_q - 1])
        down_left += min([n - r_q, c_q - 1])
        down_right += min([n - r_q, n - c_q])
    values = [up, up_left, up_right, left, right, down, down_left, down_right]
    print(values)
    return sum(values)


def main():
    print(queensAttack(column_maker))


if __name__ == '__main__':
    main()