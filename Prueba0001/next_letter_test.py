"""
    Description: This class handles the unit tests for NextLetter Class.
    Create Date: 12/03/21
    Author:      Juan castro
"""

import unittest
from next_letter import NextLetter

class NextLetterTest(unittest.TestCase):

    def setUp(self):
        self.next_letter = NextLetter()

    def test_word_empty(self):
        self.assertEqual(self.next_letter.next_word(''), '')

    def test_word_length(self):
        word = 'asdBk{%}'
        self.assertEqual(len(self.next_letter.next_word('')), len(''))
        self.assertEqual(len(self.next_letter.next_word(word)), len(word))
    
    def test_word_other_type(self):
        self.assertEqual(self.next_letter.next_word(13232), 'Please, send a string as the first parameter')
        self.assertEqual(self.next_letter.next_word(['a', 'b', 'c']), 'Please, send a string as the first parameter')

    def test_word_alphanumeric(self):
        self.assertEqual(self.next_letter.next_word('123 abcd*3'), '123 bcde*3')
        self.assertEqual(self.next_letter.next_word('**Casa 52'), '**Dbtb 52')

    def test_word_border_case(self):
        self.assertEqual(self.next_letter.next_word('aaa ** zzz'), 'bbb ** aaa')
        self.assertEqual(self.next_letter.next_word('ZZZZaaaa++++AAAA'), 'AAAAbbbb++++BBBB')

