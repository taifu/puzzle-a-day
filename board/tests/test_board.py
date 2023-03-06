import unittest

from board import Board, Pentomino


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

    def test_board_position_ESA(self):
        positions = self.board.get_positions(self.board.board, self.board.ESA)
        self.assertEqual(len(positions), 24)
        self.assertEqual(positions[0], (0, 0))
        self.assertEqual(positions[-1], (1, 4))

    def test_board_position_P(self):
        positions = self.board.get_positions(self.board.board, Pentomino.P)
        self.assertEqual(len(positions), 25)
        self.assertEqual(positions[0], (0, 0))
        self.assertEqual(positions[-1], (2, 4))

    def test_board_position_F_23_sep(self):
        board = self.board.get_date(23, 9)
        positions = self.board.get_positions(board, Pentomino.Z)
        self.assertEqual(len(positions), 16)
        self.assertEqual(positions[0], (0, 0))
        self.assertEqual(positions[-1], (4, 3))

    def test_board_matrix_rows_ESA(self):
        rows = self.board.get_matrix_rows(self.board.board, self.board.ESA)
        self.assertEqual(len(rows), 24)
        self.assertEqual(rows[0][:14], (1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1))
        self.assertFalse(any(rows[0][14:]))
        self.assertEqual(rows[-1][26:], (0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1))
        self.assertFalse(any(rows[-1][:26]))
        #self.assertEqual(rows[0][:9], (1, 1, 1, 0, 0, 0, 1, 1, 1))
        #self.assertFalse(any(rows[0][9:]))

    def test_board_matrix_all_rows_ESA(self):
        #TODO
        rows = self.board.get_matrix_all_rows(self.board.board, self.board.ESA)
        self.assertEqual(len(rows), 48)
        self.assertEqual(rows[0][:14], (1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1))
        self.assertFalse(any(rows[0][14:]))
        self.assertEqual(rows[-1][33:], (1, 1, 1, 0, 0, 0, 0, 1, 1, 1))
        self.assertFalse(any(rows[-1][:33]))
        #self.assertEqual(rows[0][:9], (1, 1, 1, 0, 0, 0, 1, 1, 1))
        #self.assertFalse(any(rows[0][9:]))
