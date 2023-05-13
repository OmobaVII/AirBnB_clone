#!/usr/bin/python3
"""This is the Unittest for the BaseModel class"""

import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """tests for the BaseModel Class"""

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        my_model = BaseModel()
        my_model.name = "Omoba"
        my_model.my_number = 89
        self.assertEqual(str(type(my_model)), "<class 'models.base_model.BaseModel'>")
        self.assertEqual(type(my_model), BaseModel)
        self.assertTrue(isinstance(my_model, BaseModel))
        self.assertTrue(issubclass(type(my_model), BaseModel))
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_doc(self):
        """checking if functions are documented"""
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__doc__)

    def test_methods(self):
        """checking to see if the functions are present"""
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "__init__"))

    def test_save(self):
        """test the save method"""
        my_model = BaseModel()
        my_model.name = "Omoba"
        my_model.my_number = 89
        my_model.save()
        second_model = BaseModel()
        second_model.save()
        self.assertFalse(my_model.created_at is my_model.updated_at)
        self.assertNotEqual(my_model.created_at, my_model.updated_at)
        self.assertNotEqual(my_model.id, second_model.id)

    def test_to_dict(self):
        """test the to_dict method"""
        my_model = BaseModel()
        my_model.name = "Omoba"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        self.assertTrue(my_model_dict['__class__'] == 'BaseModel')
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)
        self.assertEqual(my_model.__class__.__name__, "BaseModel")


if __name__ == "__main__":
    unittest.main()
