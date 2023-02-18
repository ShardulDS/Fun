def del_col(arr_org, col):
    arr = []
    for i in arr_org:
        arr.append(i.copy())
    for i in arr:
        i.pop(col)
    return arr


def determinant(matrix):
    if len(matrix) == len(matrix[0]):
        n = len(matrix)
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            det = 0
            for i in range(n):
                if i % 2 == 0:
                    det += matrix[0][i] * determinant(del_col(matrix[1:], i))
                else:
                    det -= matrix[0][i] * determinant(del_col(matrix[1:], i))
            return det


def main():
    a = [[1, 2, 3, 5],
         [4, 5, 6, 3],
         [7, 8, 2, 8],
         [8, 7, 2, 1]]
    print(determinant(a))


if __name__ == '__main__':
    main()
