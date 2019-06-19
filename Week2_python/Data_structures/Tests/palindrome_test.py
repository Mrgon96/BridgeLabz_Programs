from Week2_python.Data_structures.Palin_deque import check_palin
import  unittest

class palin_test(unittest.TestCase):
    def test_palin_deque(self):
        result = check_palin()
        expected = True
        self.assertTrue(expected,result)


if __name__ == '__main__':
    unittest.main()