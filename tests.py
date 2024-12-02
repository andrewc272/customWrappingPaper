import unittest
from backend import pngGenerator


class TestBackendFunctions(unittest.TestCase):
    def test_getDimensions(self):
        getDimensions()

        self.assertNotEqual(height, -1)
        self.assertNotEqual(width, -1)
        self.assertNotEqual(depth, -1)



if __name__ == '__main__':
    unittest.main()
