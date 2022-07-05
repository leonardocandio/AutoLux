from . import BaseTestClass

class UserTest(BaseTestClass):
    def setUp(self):
        pass

    def test_create_success(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()