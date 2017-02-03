import unittest
import NeedlemanWunsch


class TestCreateMatrix(unittest.TestCase):
    def test1(self):
        matrix = [[0, -1, -2],
                  [-1, 0, 0],
                  [-2, 0, 0]]
        self.assertEqual(NeedlemanWunsch.create_matrix(2, 2), matrix)

    def test2(self):
        matrix = [[0, -1, -2, -3],
                  [-1, 0, 0, 0],
                  [-2, 0, 0, 0],
                  [-3, 0, 0, 0]]
        self.assertEqual(NeedlemanWunsch.create_matrix(3, 3), matrix)

    def test3(self):
        matrix = [[0, -1, -2, -3],
                  [-1, 0, 0, 0],
                  [-2, 0, 0, 0]]
        self.assertEqual(NeedlemanWunsch.create_matrix(2, 3), matrix)

    def test4(self):
        matrix = [[0, -1, -2],
                  [-1, 0, 0],
                  [-2, 0, 0],
                  [-3, 0, 0]]
        self.assertEqual(NeedlemanWunsch.create_matrix(3, 2), matrix)

    def test5(self):
        matrix = [[0, -1, -2],
                  [-1, 0, 0],
                  [-2, 0, 0],
                  [-3, 0, 0],
                  [-4, 0, 0]]
        self.assertEqual(NeedlemanWunsch.create_matrix(4, 2), matrix)

    def test6(self):
        matrix = [[0, -1, -2, -3, -4],
                  [-1, 0, 0, 0, 0],
                  [-2, 0, 0, 0, 0]]
        self.assertEqual(NeedlemanWunsch.create_matrix(2, 4), matrix)

        # def test7(self):
        #     matrix = [[0, -2, -4, -6],
        #               [-2, 0, 0, 0],
        #               [-4, 0, 0, 0],
        #               [-6, 0, 0, 0]]
        #     d = -2
        #     self.assertEqual(NeedlemanWunsch.create_matrix(3, 3), matrix)


class TestF(unittest.TestCase):
    # diagonal match
    def test1(self):
        matrix = [[0, -1, -2],
                  [-1, 0, 0],
                  [-2, 0, 0]]
        list1 = 'aa'
        list2 = 'aa'

        self.assertEqual(NeedlemanWunsch.f(1, 1, matrix, list1, list2), 1)

    # diagonal mismatch
    def test2(self):
        matrix = [[0, -1, -2],
                  [-1, 0, 0],
                  [-2, 0, 0]]
        list1 = 'aa'
        list2 = 'ba'

        self.assertEqual(NeedlemanWunsch.f(1, 1, matrix, list1, list2), -1)

    # left
    def test3(self):
        matrix = [[0, -1, -2],
                  [-1, 1, 0],
                  [-2, 0, 0]]
        list1 = 'aa'
        list2 = 'aa'

        self.assertEqual(NeedlemanWunsch.f(1, 2, matrix, list1, list2), 0)

    # up
    def test4(self):
        matrix = [[0, -1, -2],
                  [-1, 1, 0],
                  [-2, 0, 0],
                  [-3, 0, 0]]
        list1 = 'aza'
        list2 = 'aa'

        self.assertEqual(NeedlemanWunsch.f(2, 1, matrix, list1, list2), 0)


class TestFillMatrix(unittest.TestCase):
    def test1(self):
        matrix = [[0, -1, -2, -3, -4, -5, -6, -7],
                  [-1, 0, 0, 0, 0, 0, 0, 0],
                  [-2, 0, 0, 0, 0, 0, 0, 0],
                  [-3, 0, 0, 0, 0, 0, 0, 0],
                  [-4, 0, 0, 0, 0, 0, 0, 0],
                  [-5, 0, 0, 0, 0, 0, 0, 0],
                  [-6, 0, 0, 0, 0, 0, 0, 0],
                  [-7, 0, 0, 0, 0, 0, 0, 0]]
        filled_matrix = [[0, -1, -2, -3, -4, -5, -6, -7],
                         [-1, 1, 0, -1, -2, -3, -4, -5],
                         [-2, 0, 0, 1, 0, -1, -2, -3],
                         [-3, -1, -1, 0, 2, 1, 0, -1],
                         [-4, -2, -2, -1, 1, 1, 0, -1],
                         [-5, -3, -3, -1, 0, 0, 0, -1],
                         [-6, -4, -2, -2, -1, -1, 1, 0],
                         [-7, -5, -3, -1, -2, -2, 0, 0]]
        list1 = "GATTACA"
        list2 = "GCATGCU"

        NeedlemanWunsch.fill_matrix(list1, list2, matrix)
        self.assertEqual(matrix, filled_matrix)


class TestAlignment(unittest.TestCase):
    def test1(self):
        filled_matrix = [[0, -1, -2, -3, -4, -5, -6, -7],
                         [-1, 1, 0, -1, -2, -3, -4, -5],
                         [-2, 0, 0, 1, 0, -1, -2, -3],
                         [-3, -1, -1, 0, 2, 1, 0, -1],
                         [-4, -2, -2, -1, 1, 1, 0, -1],
                         [-5, -3, -3, -1, 0, 0, 0, -1],
                         [-6, -4, -2, -2, -1, -1, 1, 0],
                         [-7, -5, -3, -1, -2, -2, 0, 0]]
        list1 = "GATTACA"
        list2 = "GCATGCU"

        alignment = NeedlemanWunsch.do_alignment(list1, list2, filled_matrix)

        self.assertEqual(alignment, [['G', '-', 'A', 'T', 'T', 'A', 'C', 'A'],
                                     ['|', ' ', '|', '|', '.', ' ', '|', '.'],
                                     ['G', 'C', 'A', 'T', 'G', '-', 'C', 'U']])
