import unittest
import sys


if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('.', 'test_*')
    test_runner = unittest.TextTestRunner(resultclass=unittest.TextTestResult)
    result = test_runner.run(test_suite)
    sys.exit(not result.wasSuccessful())
