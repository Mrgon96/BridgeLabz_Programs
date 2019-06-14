from ..utility import utility
import unittest

class anagramTest(unittest.TestCase):

    def test_Anagram_True(self):
        result = utility.isAnagram('dam','mad')
        expected = True
        self.assertTrue(expected,result)

    def test_Anagram_False(self):
        result = utility.isAnagram('test', 'best')
        expected = False
        self.assertFalse(expected, result)


if __name__== '__main__':
    unittest.main()

