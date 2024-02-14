#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_init(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_size_property(self):
        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_str(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_update_with_args(self):
        square = Square(5, 2, 3, 1)
        square.update(4, 6, 7, 8)
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_update_with_kwargs(self):
        square = Square(5, 2, 3, 1)
        square.update(id=4, size=6, x=7, y=8)
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        dictionary = square.to_dictionary()
        expected = {"id": 1, "size": 5, "x": 2, "y": 3}
        self.assertEqual(dictionary, expected)

if __name__ == '__main__':
    unittest.main()
