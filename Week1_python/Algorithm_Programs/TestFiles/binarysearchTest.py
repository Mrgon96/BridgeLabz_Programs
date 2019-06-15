from Week1_python.Algorithm_Programs.utility import utility
import unittest



class BinarySearchTest(unittest.TestCase):
    def testbinarysearchTest(self):
        result = utility.Bint([1,2,3,4],0,3,3)
        expected = 1
        self.assertTrue(expected,result)

if __name__=='__main__':
    unittest.main()
