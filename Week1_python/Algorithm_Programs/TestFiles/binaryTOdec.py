import Week1_python.Algorithm_Programs.binary_to_dec as bd
import unittest

class binaryTodec(unittest.TestCase):
    def testbtod(self):
        result = bd.Decimal(1010)
        expected = 10
        self.assertTrue(expected,result)


if __name__=='__main__':
    unittest.main()
