m = 1
d = -1
s = -1
def create_matrix(length1, length2):
    matrix = [[0 for x in range(length2 + 1)] for y in range(length1 + 1)]
    for i in range(1, length2 + 1):
        matrix[0][i] = i*d

    for i in range(1, length1 + 1):
        matrix[i][0] = i*d

    return matrix


def f(i, j, mem, list1, list2):
    up = mem[i - 1][j] + d
    left = mem[i][j - 1] + d
    diag = mem[i - 1][j - 1] + (m if list1[i - 1] == list2[j - 1] else s)

    return max(0, up, left, diag)


def fill_matrix(list1, list2, matrix):
    end1 = len(list1) + 1
    end2 = len(list2) + 1
    r1 = range(1, end1)
    r2 = range(1, end2)
    for row in r1:
        for col in r2:
            matrix[row][col] = f(row, col, matrix, list1, list2)