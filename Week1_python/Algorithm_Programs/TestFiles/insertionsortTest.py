from ..utility import utility
import unittest

class insertionsortTest(unittest.Test):
    def testInsertionsortTest(self):
        result = utility.insertsort([8,4,1,7,5,6,3,2]),[1,2,3,4,5,6,7,8]
        expected = True
        self.assertTrue(expected,result)


if __name__=='__main__':
    unittest.main()