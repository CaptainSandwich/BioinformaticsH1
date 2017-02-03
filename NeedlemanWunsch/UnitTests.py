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
                  [-3, 0 ,0]]
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


class TestFillMatrix(unittest.TestCase):
    def test1(self):
