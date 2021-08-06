import unittest

class ttttt(unittest.TestCase):
    def test_case1(self):
        pass

    def test_case2(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([ttttt("test_case1"),ttttt("test_case2")])
    unittest.TextTestRunner().run(suite)