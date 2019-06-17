from Week2_python.Data_structures.calender import day
import unittest

class calendertest(unittest.TestCase):

    def testcalender(self):
        result = day(1,2,2019)
        expected = 2
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()