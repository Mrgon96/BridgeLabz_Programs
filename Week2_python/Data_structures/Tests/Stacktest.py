from Week2_python.Data_structures.Arithematic_stack import balance_eq
import unittest

class arithmatic_test(unittest.TestCase):

    def test_stack(self):
        result = balance_eq()
        expected = True
        self.assertTrue(expected,result)

    def test_stack_n(self):
        result = balance_eq()
        expected = False
        self.assertNotEqual(expected,result)


if __name__ == '__main__':
    unittest.main()