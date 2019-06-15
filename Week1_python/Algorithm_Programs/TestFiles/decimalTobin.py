import Week1_python.Algorithm_Programs.dec_to_binary as db
import unittest

class dectobinary(unittest.TestCase):
    def testdTOb(self):
        result = db.binary(8)
        expected = 1000
        self.assertTrue(expected,result)

if __name__=="__main__":
    unittest.main()