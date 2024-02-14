#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_init_without_id(self):
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_init_with_id(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_to_json_string_empty(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty(self):
        result = Base.to_json_string([{'key': 'value'}])
        self.assertEqual(result, '[{"key": "value"}]')

    def test_from_json_string_empty(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string_non_empty(self):
        result = Base.from_json_string('[{"key": "value"}]')
        self.assertEqual(result, [{'key': 'value'}])

    def test_save_to_file(self):
        obj = Base()
        Base.save_to_file([obj])
        with open("Base.json", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertEqual(content, '[{"id": 1}]')

    def test_create_rectangle(self):
        from models.rectangle import Rectangle
        dictionary = {'width': 2, 'height': 3, 'id': 1}
        obj = Base.create(**dictionary)
        self.assertIsInstance(obj, Rectangle)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.id, 1)

    def test_create_square(self):
        from models.square import Square
        dictionary = {'size': 2, 'id': 1}
        obj = Base.create(**dictionary)
        self.assertIsInstance(obj, Square)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.id, 1)

    def test_load_from_file_existing_file(self):
        obj = Base()
        Base.save_to_file([obj])
        result = Base.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Base)
        self.assertEqual(result[0].id, 1)

    def test_load_from_file_non_existing_file(self):
        result = Base.load_from_file()
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
