import unittest
import SmithWaterman


class TestCreateMatrix(unittest.TestCase):
    def test1(self):
        matrix = SmithWaterman.create_matrix(2,2)
        self.assertEqual([[0, 0, 0], [0, 0, 0], [0, 0, 0]], matrix)

    def test2(self):
        matrix = SmithWaterman.create_matrix(5,5)
        self.assertEqual([[0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0]], matrix)

    def test3(self):
        matrix = SmithWaterman.create_matrix(2,5)
        self.assertEqual([[0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],], matrix)

    def test4(self):
        matrix = SmithWaterman.create_matrix(5,2)
        self.assertEqual([[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]], matrix)


class TestAlgorithm(unittest.TestCase):
    def test1(self):
        matrix = [[0, 4, 0],
                  [0, -1, -1],
                  [0, -1, -1]]
        list1 = "bb"
        list2 = "cb"
        max = SmithWaterman.f(1, 1, matrix, list1, list2)
        self.assertEqual(max, 3)

    def test2(self):
        matrix = [[0, 0, 0],
                  [4, 0, 0],
                  [0, 0, 0]]
        list1 = "bb"
        list2 = "cb"
        max = SmithWaterman.f(1, 1, matrix, list1, list2)
        self.assertEqual(max, 3)

    def test3(self):
        matrix = [[4, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        list1 = "bb"
        list2 = "bb"
        max = SmithWaterman.f(1, 1, matrix, list1, list2)
        self.assertEqual(max, 5)

    def test4(self):
        matrix = [[4, 0, 0],
                  [0, -1, -1],
                  [0, -1, -1]]
        list1 = "bb"
        list2 = "cb"
        max = SmithWaterman.f(1, 1, matrix, list1, list2)
        self.assertEqual(max, 3)

    def test5(self):
        #             x  x  x  c  d  e
        matrix = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],  # a
                  [0, 0, 0, 0, 0, 0, 0],  # b
                  [0, 0, 0, 0, 0, 0, 0],  # c
                  [0, 0, 0, 0, 0, 0, 0],  # x
                  [0, 0, 0, 0, 0, 0, 0],  # d
                  [0, 0, 0, 0, 0, 0, 0],  # e
                  [0, 0, 0, 0, 0, 0, 0]]  # x
        list1 = "abcxdex"
        list2 = "xxxcde"
        max = SmithWaterman.f(4, 1, matrix, list1, list2)
        self.assertEqual(max, 1)

    def test6(self):
        #             x  x  x  c  d  e
        matrix = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],  # a
                  [0, 0, 0, 0, 0, 0, 0],  # b
                  [0, 0, 0, 0, 0, 0, 0],  # c
                  [0, 1, 0, 0, 0, 0, 0],  # x
                  [0, 0, 0, 0, 0, 0, 0],  # d
                  [0, 0, 0, 0, 0, 0, 0],  # e
                  [0, 0, 0, 0, 0, 0, 0]]  # x
        list1 = "abcxdex"
        list2 = "xxxcde"
        max = SmithWaterman.f(4, 2, matrix, list1, list2)
        self.assertEqual(max, 1)

    def test7(self):
        #             x  x  x  c  d  e
        matrix = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],  # a
                  [0, 0, 0, 0, 0, 0, 0],  # b
                  [0, 0, 0, 0, 0, 0, 0],  # c
                  [0, 0, 0, 0, 0, 0, 0],  # x
                  [0, 0, 0, 0, 0, 0, 0],  # d
                  [0, 0, 0, 0, 0, 0, 0],  # e
                  [0, 0, 0, 0, 0, 0, 0]]  # x
        list1 = "abcxdex"
        list2 = "xxxcde"
        max = SmithWaterman.f(3, 4, matrix, list1, list2)
        self.assertEqual(max, 1)

    def test8(self):
        #             x  x  x  c  d  e
        matrix = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],  # a
                  [0, 0, 0, 0, 0, 0, 0],  # b
                  [0, 0, 0, 0, 1, 0, 0],  # c
                  [0, 0, 0, 0, 0, 0, 0],  # x
                  [0, 0, 0, 0, 0, 0, 0],  # d
                  [0, 0, 0, 0, 0, 0, 0],  # e
                  [0, 0, 0, 0, 0, 0, 0]]  # x
        list1 = "abcxdex"
        list2 = "xxxcde"
        max = SmithWaterman.f(3, 5, matrix, list1, list2)
        self.assertEqual(max, 0)

    def test9(self):
        #             x  x  x  c  d  e
        matrix = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],  # a
                  [0, 0, 0, 0, 0, 0, 0],  # b
                  [0, 0, 0, 0, 1, 0, 0],  # c
                  [0, 1, 1, 1, 0, 0, 0],  # x
                  [0, 0, 0, 0, 0, 1, 0],  # d
                  [0, 0, 0, 0, 0, 0, 0],  # e
                  [0, 0, 0, 0, 0, 0, 0]]  # x
        list1 = "abcxdex"
        list2 = "xxxcde"
        max = SmithWaterman.f(6, 6, matrix, list1, list2)
        self.assertEqual(max, 2)

    def test10(self):
        #             T  A  C  G  G  G  T  A  T
        matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],  # G
                  [0, 0, 0, 0, 1, 2, 2, 0, 0, 0],  # G
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # C
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # G
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # T
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # C
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # G
        list1 = "GGACGTACG"
        list2 = "TACGGGTAT"
        max = SmithWaterman.f(2, 7, matrix, list1, list2)
        self.assertEqual(max, 1)

    def test11(self):
        #             T  A  C  G  G  G  T  A  T
        matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],  # G
                  [0, 0, 0, 0, 1, 2, 2, 1, 0, 0],  # G
                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # A
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # C
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # G
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # T
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # C
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # G
        list1 = "GGACGTACG"
        list2 = "TACGGGTAT"
        max = SmithWaterman.f(3, 5, matrix, list1, list2)
        self.assertEqual(max, 1)


class TestFillMatrix(unittest.TestCase):

    def test1(self):
        #             T  A  C  G  G  G  T  A  T
        matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # G
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # G
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # C
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # G
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # T
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # C
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # G

        #                    T  A  C  G  G  G  T  A  T
        filled_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],  # G
                         [0, 0, 0, 0, 1, 2, 2, 1, 0, 0],  # G
                         [0, 0, 1, 0, 0, 1, 1, 1, 2, 1],  # A
                         [0, 0, 0, 2, 1, 0, 0, 0, 1, 1],  # C
                         [0, 0, 0, 1, 3, 2, 1, 0, 0, 0],  # G
                         [0, 1, 0, 0, 2, 2, 1, 2, 1, 1],  # T
                         [0, 0, 2, 1, 1, 1, 1, 1, 3, 2],  # A
                         [0, 0, 1, 3, 2, 1, 0, 0, 2, 2],  # C
                         [0, 0, 0, 2, 4, 3, 2, 1, 1, 1]]  # G
        list1 = "GGACGTACG"
        list2 = "TACGGGTAT"
        SmithWaterman.fill_matrix(list1, list2, matrix)
        self.assertEqual(matrix, filled_matrix)

    def test2(self):
        #             x  x  c  a  d  e
        matrix = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],  # a
                  [0, 0, 0, 0, 0, 0, 0],  # b
                  [0, 0, 0, 0, 0, 0, 0],  # c
                  [0, 0, 0, 0, 0, 0, 0],  # a
                  [0, 0, 0, 0, 0, 0, 0],  # d
                  [0, 0, 0, 0, 0, 0, 0],  # e
                  [0, 0, 0, 0, 0, 0, 0]]  # x

        #                    x  x  c  a  d  e
        filled_matrix = [[0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 1, 0, 0],  # a
                         [0, 0, 0, 0, 0, 0, 0],  # b
                         [0, 0, 0, 1, 0, 0, 0],  # c
                         [0, 0, 0, 0, 2, 1, 0],  # a
                         [0, 0, 0, 0, 1, 3, 2],  # d
                         [0, 0, 0, 0, 0, 2, 4],  # e
                         [0, 1, 1, 0, 0, 1, 3]]  # x
        list1 = "abcadex"
        list2 = "xxcade"
        SmithWaterman.fill_matrix(list1, list2, matrix)
        self.assertEqual(matrix, filled_matrix)


class TestDoAlignment(unittest.TestCase):
    def test1(self):
        #                    x  x  x  c  d  e
        filled_matrix = [[0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],  # a
                         [0, 0, 0, 0, 0, 0, 0],  # b
                         [0, 0, 0, 0, 2, 1, 0],  # c
                         [0, 2, 2, 2, 1, 1, 0],  # x
                         [0, 1, 1, 1, 1, 3, 2],  # d
                         [0, 0, 0, 0, 0, 2, 5],  # e
                         [0, 2, 2, 2, 1, 1, 4]]  # x

        list1 = "abcxdex"
        list2 = "xxxcde"

        m = 2
        s = -1
        d = -1

        alignment = SmithWaterman.do_alignment(list1, list2, filled_matrix)

        self.assertEqual(alignment, [['c', 'x', 'd', 'e'], ['|', ' ', '|', '|'], ['c', '-', 'd', 'e']])

    def test2(self):
        #                    T  A  C  G  G  G  T  A  T
        filled_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],  # G
                         [0, 0, 0, 0, 1, 2, 2, 1, 0, 0],  # G
                         [0, 0, 1, 0, 0, 1, 1, 1, 2, 1],  # A
                         [0, 0, 0, 2, 1, 0, 0, 0, 1, 1],  # C
                         [0, 0, 0, 1, 3, 2, 1, 0, 0, 0],  # G
                         [0, 1, 0, 0, 2, 2, 1, 2, 1, 1],  # T
                         [0, 0, 2, 1, 1, 1, 1, 1, 3, 2],  # A
                         [0, 0, 1, 3, 2, 1, 0, 0, 2, 2],  # C
                         [0, 0, 0, 2, 4, 3, 2, 1, 1, 1]]  # G
        list1 = "GGACGTACG"
        list2 = "TACGGGTAT"

        alignment = SmithWaterman.do_alignment(list1, list2, filled_matrix)

        self.assertEqual(alignment, [['T', 'A', 'C', 'G'], ['|', '|', '|', '|'], ['T', 'A', 'C', 'G']])

    def test3(self):
        #                    G  G  A  C  A  A  A  C  G
        filled_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # G
                         [0, 1, 2, 1, 0, 0, 0, 0, 0, 1],  # G
                         [0, 0, 1, 3, 2, 1, 1, 1, 0, 0],  # A
                         [0, 0, 0, 2, 4, 3, 2, 1, 1, 0],  # C
                         [0, 1, 1, 1, 3, 3, 2, 1, 0, 1],  # G
                         [0, 0, 0, 0, 2, 2, 2, 1, 0, 0],  # T
                         [0, 0, 0, 1, 1, 3, 3, 3, 2, 1],  # A
                         [0, 0, 0, 0, 1, 2, 2, 2, 4, 3],  # C
                         [0, 1, 1, 0, 0, 1, 1, 1, 3, 5]]  # G
        list1 = "GGACGTACG"
        list2 = "GGACAAACG"

        alignment = SmithWaterman.do_alignment(list1, list2, filled_matrix)

        self.assertEqual(alignment, [['G', 'G', 'A', 'C', 'G', 'T', 'A', 'C', 'G'],
                                     ['|', '|', '|', '|', '.', '.', '|', '|', '|'],
                                     ['G', 'G', 'A', 'C', 'A', 'A', 'A', 'C', 'G']])


class TestGetMax(unittest.TestCase):
    def test1(self):
        #                    x  x  x  c  d  e
        filled_matrix = [[0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],  # a
                         [0, 0, 0, 0, 0, 0, 0],  # b
                         [0, 0, 0, 0, 2, 1, 0],  # c
                         [0, 2, 2, 2, 1, 1, 0],  # x
                         [0, 1, 1, 1, 1, 3, 2],  # d
                         [0, 0, 0, 0, 0, 2, 5],  # e
                         [0, 2, 2, 2, 1, 1, 4]]  # x

        list1 = "abcxdex"
        list2 = "xxxcde"

        self.assertEqual(SmithWaterman.get_max(list1, list2, filled_matrix), [6,6])