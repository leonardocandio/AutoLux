import unittest

class UserTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_success(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()