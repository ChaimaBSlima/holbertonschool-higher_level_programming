#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_init(self):
        rect = Rectangle(10, 20, 2, 3, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_width_property(self):
        rect = Rectangle(10, 20)
        rect.width = 30
        self.assertEqual(rect.width, 30)

    def test_height_property(self):
        rect = Rectangle(10, 20)
        rect.height = 25
        self.assertEqual(rect.height, 25)

    def test_x_property(self):
        rect = Rectangle(10, 20, 2, 3)
        rect.x = 5
        self.assertEqual(rect.x, 5)

    def test_y_property(self):
        rect = Rectangle(10, 20, 2, 3)
        rect.y = 8
        self.assertEqual(rect.y, 8)

    def test_area(self):
        rect = Rectangle(10, 20)
        self.assertEqual(rect.area(), 200)

    def test_display(self):
        rect = Rectangle(3, 2, 1, 1)
        self.assertEqual(rect.display(), "\n ###\n ###\n")

    def test_str(self):
        rect = Rectangle(10, 20, 2, 3, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/3 - 10/20")

    def test_update_with_args(self):
        rect = Rectangle(10, 20, 2, 3, 1)
        rect.update(4, 5, 6, 7, 8)
        self.assertEqual(rect.id, 4)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 8)

    def test_update_with_kwargs(self):
        rect = Rectangle(10, 20, 2, 3, 1)
        rect.update(id=4, width=5, height=6, x=7, y=8)
        self.assertEqual(rect.id, 4)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 8)

    def test_to_dictionary(self):
        rect = Rectangle(10, 20, 2, 3, 1)
        dictionary = rect.to_dictionary()
        expected = {"id": 1, "width": 10, "height": 20, "x": 2, "y": 3}
        self.assertEqual(dictionary, expected)

if __name__ == '__main__':
    unittest.main()
