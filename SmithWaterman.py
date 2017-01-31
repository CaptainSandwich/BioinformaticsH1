from enum import Enum

def get_file_data(prompt):
    filename = input(prompt)
    file = open(filename, 'r')
    return file.read()

class Direction(Enum):
    NONE = 0,
    UP = 1,
    LEFT = 2,
    DIAGONAL = 3

m = 1
d = s = -1


def sigma(i, j, mem):
    if mem[i][j] == mem[i-1][j-1]:
        return m
    else:
        return d


def f(i, j, mem):
    if mem[i][j] >= 0:
        return mem[i][j]
    else:
       return max(0,
                  f(i - 1, j) - d,
                  f(i, j - 1) - d,
                  f(i - 1, j - 1) + sigma(i, j, mem))


file1 = get_file_data("Enter first file name: ")
file2 = get_file_data("Enter second file name: ")

file1list = list(file1)
file2list = list(file2)

matrix = [[-1 for x in range(len(file1list) + 1)] for y in range(len(file2list) + 1)]
backtrace = [[Direction.NONE for x in range(len(file1list) + 1)] for y in range(len(file2list) + 1)]

for row in range(1, len(file1list)):
    for col in range(1, len(file2list)):
        matrix[row][col] = f(row, col, matrix)
        if matrix[row][col] == matrix[row - 1][col] - d:
            backtrace[row][col] = Direction.UP
        elif matrix[row][col] == matrix[row][col - 1] - d:
            backtrace[row][col] = Direction.LEFT
        else:
            backtrace[row][col] = Direction.DIAGONAL


