m = 1
d = -1
s = -1


def get_file_data(prompt):
    filename = input(prompt)
    file = open(filename, 'r')
    return file.read()


def create_matrix(length1, length2):
    matrix = [[0 for x in range(length2 + 1)] for y in range(length1 + 1)]
    return matrix


def f(i, j, mem, list1, list2):
    up = mem[i - 1][j] + d
    left = mem[i][j - 1] + d
    diag = mem[i - 1][j - 1] + (m if list1[i - 1] == list2[j - 1] else s)

    return max(0, up, left, diag)


def fill_matrix(list1, list2, matrix):
    end1 = len(list1) + 1
    end2 = len(list2) + 1
    for row in range(1, end1):
        for col in range(1, end2):
            matrix[row][col] = f(row, col, matrix, list1, list2)


def get_max(list1, list2, matrix):
    max_row = 0
    max_col = 0
    max_val = 0

    for row in range(1, len(list1) + 1):
        for col in range(1, len(list2) + 1):
            if matrix[row][col] > max_val:
                max_val = matrix[row][col]
                max_row = row
                max_col = col

    return [max_row, max_col]


def do_alignment(list1, list2, matrix):

    max = get_max(list1, list2, matrix)

    row = max[0]
    col = max[1]
    new_list_1 = []
    new_list_2 = []
    aligner = []

    while matrix[row][col] != 0:
        if matrix[row][col] == (matrix[row - 1][col] + d):
            new_list_2 = ['-'] + new_list_2
            new_list_1 = [list1[row - 1]] + new_list_1
            row -= 1
            aligner = [' '] + aligner
        elif matrix[row][col] == (matrix[row][col - 1] + d):
            new_list_2 = [list2[col - 1]] + new_list_2
            new_list_1 = ['-'] + new_list_1
            col -= 1
            aligner = [' '] + aligner
        else:
            if list1[row - 1] == list2[col - 1]:
                aligner = ['|'] + aligner
            else:
                aligner = ['.'] + aligner
            new_list_1 = [list1[row - 1]] + new_list_1
            new_list_2 = [list2[col - 1]] + new_list_2
            col -= 1
            row -= 1

    return [new_list_1, aligner, new_list_2]

# file1 = get_file_data("Enter first file name: ")
# file2 = get_file_data("Enter second file name: ")
#
# file1list = list(file1)
# file2list = list(file2)
#
# file1len = len(file1list)
# file2len = len(file2list)

# i = 0
#
# length = str(file1len * file2len)
#
# end1 = file2len + 1
# end2 = file1len + 1
# for row in range(1, end1):
#     for col in range(1, end2):
#         matrix[row][col] = f(row, col, matrix)
#
# max_row = 0
# max_col = 0
# max_val = 0
#
# for row in range(1, len(file2list) + 1):
#     for col in range(1, len(file1list) + 1):
#         if matrix[row][col] > max_val:
#             max_val = matrix[row][col]
#             max_row = row
#             max_col = col

# col = max_col
# row = max_row
# new_list_1 = []
# new_list_2 = []
# backtrace = []
# while matrix[row][col] != 0:
#     if matrix[row][col] == (matrix[row - 1][col] - 1):
#         new_list_1 = [' '] + new_list_1
#         new_list_2 += [file2list[col]]
#         row -= 1
#         backtrace.append(Direction.UP)
#     elif matrix[row][col] == (matrix[row][col - 1]):
#         new_list_1 += [file1list[row]]
#         new_list_2 = [' '] + new_list_2
#         col -= 1
#         backtrace.append(Direction.LEFT)
#     else:
#         new_list_1 = [file1list[col - 1]] + new_list_1
#         new_list_2 = [file2list[row - 1]] + new_list_2
#         col -= 1
#         row -= 1
#         backtrace.append(Direction.DIAGONAL)

# if col < row:
#     print("Column was less than row!")
#     for i in range(0, max_col):
#         new_list_1 = new_list_1 + [file1list[i]]
#     for i in range(1, row):
#         new_list_1 = [' '] + new_list_1
#         new_list_2 = new_list_2 + [file2list[i]]
#     for i in range(max_col, len(file1list)):
#         new_list_1 = new_list_1 + [file1list[i]]
# else:
#     print("Column was greater than row!")
#     for i in range(1, col):
#         new_list_1 = new_list_1 + [file1list[i]]
#         new_list_2 = [' '] + new_list_2
#     for i in range(col, file1len):
#         new_list_1 = new_list_1 + [file1list[i]]
#     for i in range(max_row, len(file2list)):
#         new_list_2 = new_list_2 + [file2list[i]]

# if col < row:
#     for i in range(0,row):
#         new_list_1 = [' '] + new_list_1
#     new_list_1 = new_list_1 + file1list[row - 1:]
#     new_list_2 = file2list[0:max_col + 1] + new_list_2
# else:
#     for i in range(0,col):
#         new_list_2 = [' '] + new_list_2
#     new_list_1 = file1list[0:max_row] + new_list_1
#     new_list_2 = new_list_2 + file2list[col - 1:]


# print(''.join(new_list_1))
# print(''.join(new_list_2))
# print(np.matrix(matrix))
# print(backtrace)
# print((max_col, max_row))
# print(max_val)
