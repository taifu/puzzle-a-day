import unittest

from board import Board, Pentomino


class TestRotateReflect(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_rotate_I_1(self):
        self.assertEqual(self.board.rotate(Pentomino.I),
                 ((1, 1, 1, 1, 1),)) 

    def test_rotate_I_2(self):
        self.assertEqual(self.board.rotate(self.board.rotate(Pentomino.I)),
                 ((1,),
                  (1,),
                  (1,),
                  (1,),
                  (1,)))

    def test_rotate_I_3(self):
        self.assertEqual(self.board.rotate(self.board.rotate(self.board.rotate(Pentomino.I))),
                 ((1, 1, 1, 1, 1),)) 

    def test_rotations_X(self):
        rot = Pentomino.X[:]
        rotations = set((rot,))
        for x in range(3):
            rot = self.board.rotate(rot)
            rotations.add(rot)
        self.assertEqual(len(rotations), 1)

    def test_rotations_V(self):
        rot = Pentomino.V[:]
        rotations = set((rot,))
        for x in range(3):
            rot = self.board.rotate(rot)
            rotations.add(rot)
        self.assertEqual(len(rotations), 4)

    def test_reflect_X(self):
        self.assertEqual(Pentomino.X, self.board.reflect(Pentomino.X))

    def test_reflect_X_double(self):
        self.assertEqual(Pentomino.X, self.board.reflect(self.board.reflect(Pentomino.X)))

    def test_reflect_I_double(self):
        self.assertEqual(Pentomino.I, self.board.reflect(self.board.reflect(Pentomino.I)))

    def test_reflect_V_double(self):
        self.assertEqual(Pentomino.V, self.board.reflect(self.board.reflect(Pentomino.V)))

    def test_rotations_reflections_X(self):
        rot = Pentomino.X[:]
        rotations_reflections = set()
        for x in range(4):
            rotations_reflections.add(rot)
            rot = self.board.reflect(rot)
            rotations_reflections.add(rot)
            rot = self.board.rotate(self.board.reflect(rot))
        self.assertEqual(len(rotations_reflections), 1)

    def test_rotations_reflections_I(self):
        rot = Pentomino.I[:]
        rotations_reflections = set()
        for x in range(4):
            rotations_reflections.add(rot)
            rot = self.board.reflect(rot)
            rotations_reflections.add(rot)
            rot = self.board.rotate(self.board.reflect(rot))
        self.assertEqual(len(rotations_reflections), 2)

    def test_rotations_reflections_V(self):
        rot = Pentomino.V[:]
        rotations_reflections = set()
        for x in range(4):
            rotations_reflections.add(rot)
            rot = self.board.reflect(rot)
            rotations_reflections.add(rot)
            rot = self.board.rotate(self.board.reflect(rot))
        print(rotations_reflections)
        self.assertEqual(len(rotations_reflections), 4)

    def test_rotations_reflections_P(self):
        rot = Pentomino.P[:]
        rotations_reflections = set()
        for x in range(4):
            rotations_reflections.add(rot)
            rot = self.board.reflect(rot)
            rotations_reflections.add(rot)
            rot = self.board.rotate(self.board.reflect(rot))
        self.assertEqual(len(rotations_reflections), 8)

    def test_board_rotations_reflections_X(self):
        rotations_reflections = self.board.get_rotations_reflections(Pentomino.X)
        self.assertEqual(set(rotations_reflections), set((Pentomino.X,)))

