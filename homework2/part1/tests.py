import unittest
from copy import copy
from customlist import CustomList

class TestCases(unittest.TestCase):

    def setUp(self):
        self.lst1 = [1, 2, 3, 4, 5, 6, 7]
        self.lst2 = CustomList([-5, -10, 0])
        self.lst3 = CustomList()
        self.lst3.append(100)
        self.lst3.append(-500)
        self.lst4 = CustomList((29, 100, 89, 2, -9))

    def test_init(self):
        self.assertEqual(type(self.lst1), type(list()))
        self.assertEqual(type(self.lst2), type(CustomList()))
        self.assertEqual(type(self.lst3), type(CustomList()))
        self.assertEqual(type(self.lst4), type(CustomList()))
        self.assertEqual(len(self.lst1), 7)
        self.assertEqual(len(self.lst2), 3)
        self.assertEqual(len(self.lst3), 2)
        self.assertEqual(len(self.lst4), 5)

    def test_add(self):
        cpy1 = copy(self.lst1)
        cpy2 = copy(self.lst2)
        cpy3 = copy(self.lst3)
        res = self.lst1 + self.lst2
        self.assertEqual(res, CustomList([-4, -8, 3, 4, 5, 6, 7]))
        self.assertEqual(self.lst1, cpy1)
        self.assertEqual(self.lst2, cpy2)
        self.assertEqual(type(res), type(CustomList()))
        res = self.lst3 + self.lst1
        self.assertEqual(res, CustomList([101, -498, 3, 4, 5, 6, 7]))
        self.assertEqual(self.lst1, cpy1)
        self.assertEqual(self.lst3, cpy3)
        self.assertEqual(type(res), type(CustomList()))
        res = self.lst2 + self.lst3
        self.assertEqual(res, CustomList([95, -510, 0]))
        self.assertEqual(self.lst2, cpy2)
        self.assertEqual(self.lst3, cpy3)
        self.assertEqual(type(res), type(CustomList()))
       
    def test_sub(self):
        cpy1 = copy(self.lst1)
        cpy2 = copy(self.lst2)
        cpy4 = copy(self.lst4)
        res = self.lst1 - self.lst2
        self.assertEqual(res, CustomList([6, 12, 3, 4, 5, 6, 7]))
        self.assertEqual(self.lst1, cpy1)
        self.assertEqual(self.lst2, cpy2)
        self.assertEqual(type(res), type(CustomList()))
        res = self.lst4 - self.lst1
        self.assertEqual(res, CustomList([28, 98, 86, -2, -14, -6, -7]))
        self.assertEqual(self.lst1, cpy1)
        self.assertEqual(self.lst4, cpy4)
        self.assertEqual(type(res), type(CustomList()))
        res = self.lst2 - self.lst4
        self.assertEqual(res, CustomList([-34, -110, -89, -2, 9]))
        self.assertEqual(self.lst2, cpy2)
        self.assertEqual(self.lst4, cpy4)
        self.assertEqual(type(res), type(CustomList()))

    def test_comp(self):
        self.assertTrue(self.lst1 != self.lst2)
        self.assertTrue(self.lst2 == self.lst2)
        self.assertTrue(self.lst1 < self.lst4)
        self.assertTrue(self.lst2 > self.lst3)
        self.assertTrue(self.lst3 <= self.lst4)
        self.assertFalse(self.lst2 == self.lst4)
        self.assertFalse(self.lst3 >= self.lst1)
        self.assertFalse(self.lst4 <= self.lst2)
        self.assertFalse(self.lst1 > self.lst4)
        self.assertFalse(self.lst4 < self.lst4)
