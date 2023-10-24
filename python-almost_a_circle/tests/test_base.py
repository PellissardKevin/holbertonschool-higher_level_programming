#!/usr/bin/python3
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import unittest, sys, json
import os
"""Create a class for testing base class"""


class test_base(unittest.TestCase):
    """Class for testing base class"""

    @classmethod
    def setUpClass(cls):
        """setup class method"""

        cls.bs1 = Base()
        cls.bs2 = Base(100)
        cls.bs3 = Base()
        cls.rt1 = Rectangle(10, 10)
        cls.rt2 = Rectangle(20, 20, id=1000)
        cls.rt3 = Rectangle(30, 30, 3, 3, id=100)
        cls.sq1 = Square(10)
        cls.sq2 = Square(5, 5, 4, id=200)
        cls.sq3 = Square(12, id=22)

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        sys.stdout = sys.__stdout__

    def test_base_cls_doc(self):
        """check if docstring for class is present"""
        self.assertIsNotNone(Base.__doc__)

    def test_base_instance_doc(self):
        """check if instance of Base is present"""
        self.assertIsNotNone(self.bs1.__doc__)
        self.assertIsNotNone(self.rt1.__doc__)
        self.assertIsNotNone(self.sq1.__doc__)

    def test_base_methods_doc(self):
        """docstring exist for all methods"""
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(Base.load_from_file.__doc__)

    def test_id(self):
        """ Test check for id """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_rectangle(self):
        """ Test check for rectangle """
        R1 = Rectangle(4, 5, 6, 7)
        R1_dict = R1.to_dictionary()
        R2 = Rectangle.create(**R1_dict)
        self.assertNotEqual(R1, R2)

    def test_square(self):
        """ Test check for square creation """
        S1 = Square(44, 55, 66)
        S1_dict = S1.to_dictionary()
        S2 = Rectangle.create(**S1_dict)
        self.assertNotEqual(S1, S2)

    def test_file_rectangle(self):
        """ Test check if file loads from rectangle """
        R1 = Rectangle(33, 34, 35, 26)
        R2 = Rectangle(202, 2)
        lR = [R1, R2]
        Rectangle.save_to_file(lR)
        lR2 = Rectangle.load_from_file()
        self.assertNotEqual(lR, lR2)

    def test_file_square(self):
        """ Test check if file loads from square """
        S1 = Square(22)
        S2 = Square(44, 44, 55, 66)
        lS = [S1, S2]
        Square.save_to_file(lS)
        lS2 = Square.load_from_file()
        self.assertNotEqual(lS, lS2)

if __name__ == '__main__':
    unittest.main()
