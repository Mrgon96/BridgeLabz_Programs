from ..utility import utility
import unittest

class bubblesortTest(unittest.TestCase):

    def testbubble(self):
        result = utility.bubble([8,6,4,7,2,1,3,5]),[1,2,3,4,5,6,7,8]
        expected = True
        self.assertTrue(expected,result)


if __name__=='__main__':
    unittest.main()
