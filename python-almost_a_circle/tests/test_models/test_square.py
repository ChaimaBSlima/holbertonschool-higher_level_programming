#!/usr/bin/python3
#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    '''Tests the Square class.'''

    def setUp(self):
        '''Set up before each test method.'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Clean up after each test method.'''
        pass

    def test_class_type(self):
        '''Test Square class type.'''
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test_inheritance(self):
        '''Test if Square inherits from Base.'''
        self.assertTrue(issubclass(Square, Base))

    def test_constructor_no_args(self):
        '''Test constructor signature with no arguments.'''
        with self.assertRaises(TypeError) as e:
            Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_constructor_many_args(self):
        '''Test constructor signature with too many arguments.'''
        with self.assertRaises(TypeError) as e:
            Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 were given"
        self.assertEqual(str(e.exception), s)

    def test_instantiation(self):
        '''Test instantiation with various scenarios.'''
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Square("1")
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)


    def test_to_dictionary(self):
        '''Test to_dictionary() method signature and functionality.'''
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)


if __name__ == "__main__":
    unittest.main()
