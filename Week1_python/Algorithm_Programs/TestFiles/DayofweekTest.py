from ..utility import utility
import unittest

class DayofweekTest(unittest.TestCase):
    def day_correct(self):
        result = utility.Day(1,1,2019)
        expected = 'Monday'
        self.assertEquals(expected,result)


if __name__ == '__main__':
    unittest.main()


