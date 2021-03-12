"""
    Document:    DDATM-ES-0002-E
    Description: This class handles the unit tests for FillNumber Class.
    Create Date: 12/03/21
    Author:      Juan castro
"""

import unittest
from fill_numbers import FillNumbers

class FillNumbersTest(unittest.TestCase):

    def setUp(self):
        self.numbers = FillNumbers()

    def test_array_other_type(self):
        self.assertEqual(self.numbers.fill_numbers(['a', 'b', '%']), 'Please, send a list of numbers')
        self.assertEqual(self.numbers.fill_numbers([4, 6, 9, [3, 5]]), 'Please, send a list of numbers')
        self.assertEqual(self.numbers.fill_numbers(576678), 'Please, send a list of numbers')
        self.assertEqual(self.numbers.fill_numbers('576678'), 'Please, send a list of numbers')

    def test_array_empty(self):
        self.assertEqual(self.numbers.fill_numbers([]), 'Please, send a not empty array')

    def test_array_not_positive_numbers(self):
        self.assertEqual(self.numbers.fill_numbers([-1, -4, -5, -6]), 'Please, send only a positive numbers')
        self.assertEqual(self.numbers.fill_numbers([4, 25, 13, 0]), 'Please, send only a positive numbers')

    def test_array_fill(self):
        self.assertListEqual(self.numbers.fill_numbers([8, 24, 7, 98, 65]), list(range(1, 99)))
        self.assertListEqual(self.numbers.fill_numbers([38, 2, 15, 16, 21]), list(range(1, 39)))
        self.assertListEqual(self.numbers.fill_numbers([1, 2, 3, 4]), list(range(1, 5)))

    def test_array_in_result(self):
        array = [15, 21, 6, 11]
        fill_array = self.numbers.fill_numbers(array)
        for el in array:
            self.assertTrue(el in fill_array)

    def test_array_duplicates(self):
        array = [15, 17, 12, 21, 15, 56, 67, 15]
        fill_array = self.numbers.fill_numbers(array)
        for el in array:
            self.assertEqual(fill_array.count(el), 1)
