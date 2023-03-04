import unittest

from ..helpers import Pentomino, rotate, reflect


class TestRotateReflect(unittest.TestCase):
    def test_rotate_I_1(self):
        self.assertEqual(rotate(Pentomino.I),
                 ((1, 1, 1, 1, 1),)) 

    def test_rotate_I_2(self):
        self.assertEqual(rotate(rotate(Pentomino.I)),
                 ((1,),
                  (1,),
                  (1,),
                  (1,),
                  (1,)))

    def test_rotate_I_3(self):
        self.assertEqual(rotate(rotate(rotate(Pentomino.I))),
                 ((1, 1, 1, 1, 1),)) 

    def test_rotations_X(self):
        rot = Pentomino.X[:]
        rotations = set((rot,))
        for x in range(3):
            rot = rotate(rot)
            rotations.add(rot)
        self.assertEqual(len(rotations), 1)

    def test_rotations_V(self):
        rot = Pentomino.V[:]
        rotations = set((rot,))
        for x in range(3):
            rot = rotate(rot)
            rotations.add(rot)
        self.assertEqual(len(rotations), 4)

    def test_reflect_X(self):
        self.assertEqual(Pentomino.X, reflect(Pentomino.X))

    def test_reflect_X_double(self):
        self.assertEqual(Pentomino.X, reflect(reflect(Pentomino.X)))

    def test_reflect_I_double(self):
        self.assertEqual(Pentomino.I, reflect(reflect(Pentomino.I)))

    def test_reflect_V_double(self):
        self.assertEqual(Pentomino.V, reflect(reflect(Pentomino.V)))

    def test_rotations_reflections_X(self):
        rot = Pentomino.X[:]
        rotations_reflections = set()
        for x in range(4):
            rotations_reflections.add(rot)
            rot = reflect(rot)
            rotations_reflections.add(rot)
            rot = rotate(reflect(rot))
        self.assertEqual(len(rotations_reflections), 1)

    def test_rotations_reflections_I(self):
        rot = Pentomino.I[:]
        rotations_reflections = set()
        for x in range(4):
            rotations_reflections.add(rot)
            rot = reflect(rot)
            rotations_reflections.add(rot)
            rot = rotate(reflect(rot))
        self.assertEqual(len(rotations_reflections), 2)

    def test_rotations_reflections_V(self):
        rot = Pentomino.V[:]
        rotations_reflections = set()
        for x in range(4):
            rotations_reflections.add(rot)
            rot = reflect(rot)
            rotations_reflections.add(rot)
            rot = rotate(reflect(rot))
        print(rotations_reflections)
        self.assertEqual(len(rotations_reflections), 4)

    def test_rotations_reflections_P(self):
        rot = Pentomino.P[:]
        rotations_reflections = set()
        for x in range(4):
            rotations_reflections.add(rot)
            rot = reflect(rot)
            rotations_reflections.add(rot)
            rot = rotate(reflect(rot))
        print(rotations_reflections)
        self.assertEqual(len(rotations_reflections), 8)
