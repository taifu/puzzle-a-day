import unittest

from ..board import Board


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_1_jan(self):
        self.assertEqual(self.board.get_date(1, 1),
                     ((0, 1, 1, 1, 1, 1, 0), # Month Jan-Jun
                      (1, 1, 1, 1, 1, 1, 0), # Month Jul-Dec
                      (0, 1, 1, 1, 1, 1, 1), # Day 1-7
                      (1, 1, 1, 1, 1, 1, 1), # Day 8-14
                      (1, 1, 1, 1, 1, 1, 1), # Day 15-21
                      (1, 1, 1, 1, 1, 1, 1), # Day 22-28
                      (1, 1, 1, 0, 0, 0, 0), # Day 29-31
                      ))

    def test_board_31_dec(self):
        self.assertEqual(self.board.get_date(31, 12),
                     ((1, 1, 1, 1, 1, 1, 0), # Month Jan-Jun
                      (1, 1, 1, 1, 1, 0, 0), # Month Jul-Dec
                      (1, 1, 1, 1, 1, 1, 1), # Day 1-7
                      (1, 1, 1, 1, 1, 1, 1), # Day 8-14
                      (1, 1, 1, 1, 1, 1, 1), # Day 15-21
                      (1, 1, 1, 1, 1, 1, 1), # Day 22-28
                      (1, 1, 0, 0, 0, 0, 0), # Day 29-31
                      ))

    def test_board_14_jun(self):
        self.assertEqual(self.board.get_date(14, 6),
                     ((1, 1, 1, 1, 1, 0, 0), # Month Jan-Jun
                      (1, 1, 1, 1, 1, 1, 0), # Month Jul-Dec
                      (1, 1, 1, 1, 1, 1, 1), # Day 1-7
                      (1, 1, 1, 1, 1, 1, 0), # Day 8-14
                      (1, 1, 1, 1, 1, 1, 1), # Day 15-21
                      (1, 1, 1, 1, 1, 1, 1), # Day 22-28
                      (1, 1, 1, 0, 0, 0, 0), # Day 29-31
                      ))

    def test_board_23_sep(self):
        self.assertEqual(self.board.get_date(23, 9),
                     ((1, 1, 1, 1, 1, 1, 0), # Month Jan-Jun
                      (1, 1, 0, 1, 1, 1, 0), # Month Jul-Dec
                      (1, 1, 1, 1, 1, 1, 1), # Day 1-7
                      (1, 1, 1, 1, 1, 1, 1), # Day 8-14
                      (1, 1, 1, 1, 1, 1, 1), # Day 15-21
                      (1, 0, 1, 1, 1, 1, 1), # Day 22-28
                      (1, 1, 1, 0, 0, 0, 0), # Day 29-31
                      ))
