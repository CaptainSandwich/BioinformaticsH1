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


def get_file_data(prompt):
    filename = input(prompt)
    file = open(filename, 'r')
    return file.read()


def create_matrix(vertical_length, horizontal_length):
    """
    Creates and initializes a matrix of size vertical_length * horizontal_length for the Smith-Waterman algorithm

    :param int vertical_length: Length of the list representing the vertical sequence of the alignment matrix
    :param int horizontal_length: Length of the list representing the horizontal sequence of the alignment matrix

    :return matrix: A two dimensional list representing the alignment table initialized such that each element = 0
    """
    matrix = [[0 for x in range(horizontal_length + 1)] for y in range(vertical_length + 1)]
    return matrix


def f(row, column, matrix, vertical_list, horizontal_list):
    """
    Finds the optimal alignment for the subsequences vertical_list[0:row-1] and horizontal_list[0:column-1]
    according to the Smith-Waterman algorithm

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

    return max(0, up, left, diag)


def fill_matrix(vertical_list, horizontal_list, matrix):
    """
    Fills the alignment scoring matrix according to the Smith-Waterman algorithm

    :param list vertical_list:
    :param list horizontal_list:
    :param list matrix: The alignment scoring matrix
    """
    end1 = len(vertical_list) + 1
    end2 = len(horizontal_list) + 1
    r1 = range(1, end1)
    r2 = range(1, end2)
    for row in r1:
        for col in r2:
            matrix[row][col] = f(row, col, matrix, vertical_list, horizontal_list)


def get_max(matrix):
    """
    Finds the location of the optimal local alignment score of the alignment matrix

    :param matrix: The alignment scoring matrix
    :return max_coords: The row and column of the optimal local alignment score of the matrix
    """
    max_row = 0
    max_col = 0
    max_val = 0

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[row][col] > max_val:
                max_val = matrix[row][col]
                max_row = row
                max_col = col

    max_coords = [max_row, max_col]
    return max_coords


def do_alignment(vertical_list, horizontal_list, matrix):
    """
    Generates three lists representing the optimal local alignment of vertical_list and horizontal_list,
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

    max_coords = get_max(matrix)
    row = max_coords[0]
    col = max_coords[1]
    new_list_1 = []
    new_list_2 = []
    aligner = []

    while matrix[row][col] != 0:
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

    return [new_list_1, aligner, new_list_2]
