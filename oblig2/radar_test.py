import unittest   # The test framework
import radars

class Test_login(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(len(radars.list_speeders('box_a.txt', 'box_b.txt', 60, 5)), 15)
 

if __name__ == '__main__':
    unittest.main()
