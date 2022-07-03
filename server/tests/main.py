import unittest

from test_post import PostTest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(PostTest())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
