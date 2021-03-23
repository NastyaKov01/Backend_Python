"""Testing module"""
import unittest
from custommeta import CustomMeta


class TestCases(unittest.TestCase):
    """Testing class"""
    def test_1(self):
        """First test"""
        class CustomClass(metaclass=CustomMeta):
            x, y = 50, -100
            z = "qwerty"
            
            def add(self):
                return x + y
            
            def line(self):
                return 100

        inst = CustomClass()
        for attr in dir(inst):
            if not attr.startswith('_'):
                self.assertTrue(attr.startswith('custom'))

    def test_2(self):
        """Second test"""
        class CustomClass(metaclass=CustomMeta):
            first, second = 1, 2
            name = "class"
            lst = [1,2,3,4]

            def comp(self):
                return first < second

            def truefun(self):
                return True

        inst = CustomClass()
        for attr in dir(inst):
            if not attr.startswith('_'):
                self.assertTrue(attr.startswith('custom'))

