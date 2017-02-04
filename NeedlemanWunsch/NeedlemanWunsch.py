#: Match score
m = 1

#: Deletion penalty
d = -1

#: Mismatch penalty
s = -1


def set_alignment_scores(new_m, new_d, new_s):
    """
    Sets the scoring variables for the Needleman-Wunsch algorithm

    :param new_m: New match score
    :param new_d: New deletion score
    :param new_s: New mismatch score
    """
    global m, d, s
    m = new_m
    d = new_d
    s = new_s


def create_matrix(vertical_length, horizontal_length):
    """
    Creates and initializes a matrix of size vertical_length * horizontal_length for the Needleman-Wunsch algorithm

    :param int vertical_length: Length of the list representing the vertical sequence of the alignment matrix
    :param int horizontal_length: Length of the list representing the horizontal sequence of the alignment matrix

    :return matrix: A two dimensional list representing the alignment table initialized such that
        matrix[0][0] = 0,
        matrix[0][column] = column * d
        matrix[row][0] = row * d
    """
    matrix = [[0 for column in range(horizontal_length + 1)] for row in range(vertical_length + 1)]
    for column in range(1, horizontal_length + 1):
        matrix[0][column] = column * d

    for row in range(1, vertical_length + 1):
        matrix[row][0] = row * d

    return matrix


def f(row, column, matrix, vertical_list, horizontal_list):
    """
    Finds the optimal alignment for the subsequences vertical_list[0:row-1] and horizontal_list[0:column-1]
    according to the Needleman-Wunsch algorithm

    :param int row: Index for the row of matrix
    :param int column: Index for the column of matrix
    :param list matrix: The alignment scoring matrix
    :param list vertical_list: List representing the vertical sequence of the alignment matrix
    :param list horizontal_list: List representing the horizontal sequence of the alignment matrix
    :return local_max: The maximum score for the current subsequence
    """
    up = matrix[row - 1][column] + d
    left = matrix[row][column - 1] + d
    diag = matrix[row - 1][column - 1] + (m if vertical_list[row - 1] == horizontal_list[column - 1] else s)

    local_max = max(up, left, diag)
    return local_max


def fill_matrix(vertical_list, horizontal_list, matrix):
    """
    Fills the alignment scoring matrix according to the Needleman-Wunsch algorithm

    :param list vertical_list:
    :param list horizontal_list:
    :param list matrix: The alignment scoring matrix
    """
    row_end = len(vertical_list) + 1
    column_end = len(horizontal_list) + 1
    for row in range(1, row_end):
        for column in range(1, column_end):
            matrix[row][column] = f(row, column, matrix, vertical_list, horizontal_list)


def generate_alignment(vertical_list, horizontal_list, matrix):
    """
    Generates three lists representing the optimal global alignment of vertical_list and horizontal_list,
    such that matches line up together with '|', mismatches line up together with '.', and gaps insert '-' into the
    string with the deletion and a ' ' into the alignment string

    Example:
    The filled alignment matrix for
    vertical_list = "GATTACA"
    and
    horizontal_list = "GCATGCU"
    will yield
    [['G', '-', 'A', 'T', 'T', 'A', 'C', 'A'],
     ['|', ' ', '|', '|', '.', ' ', '|', '.'],
     ['G', 'C', 'A', 'T', 'G', '-', 'C', 'U']]

    :param list vertical_list: List representing the vertical sequence of the alignment matrix
    :param list horizontal_list: List representing the horizontal sequence of the alignment matrix
    :param list matrix: The alignment scoring matrix
    :return alignment:
    """
    row = len(vertical_list)
    col = len(horizontal_list)
    new_list_1 = []
    new_list_2 = []
    aligner = []

    while row != 0 or col != 0:
        if matrix[row][col] == (matrix[row - 1][col] + d):
            new_list_2 = ['-'] + new_list_2
            new_list_1 = [vertical_list[row - 1]] + new_list_1
            row -= 1
            aligner = [' '] + aligner
        elif matrix[row][col] == (matrix[row][col - 1] + d):
            new_list_2 = [horizontal_list[col - 1]] + new_list_2
            new_list_1 = ['-'] + new_list_1
            col -= 1
            aligner = [' '] + aligner
        else:
            if vertical_list[row - 1] == horizontal_list[col - 1]:
                aligner = ['|'] + aligner
            else:
                aligner = ['.'] + aligner
            new_list_1 = [vertical_list[row - 1]] + new_list_1
            new_list_2 = [horizontal_list[col - 1]] + new_list_2
            col -= 1
            row -= 1

    alignment = [new_list_1, aligner, new_list_2]
    return alignment
