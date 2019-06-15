import Week1_python.Algorithm_Programs.binary_nibble as bn
import unittest

class nibbleTest:
    def testnibbleTest(self):
        result = bn.SwapNibble(100)
        expected = 70
        self.assrtTrue(expected,result)


if __name__=='__main__':
    unittest.main()
