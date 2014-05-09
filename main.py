import random
import unittest
import sys

sys.path.insert(0,'/usr/lib/pyshared/python2.7')

import cv2
import numpy as np

from cvprocessor import isWhiteImage

"""What is up"""
class TestSequenceFunctions(unittest.TestCase):

    def test_white(self):
        self.assertTrue(isWhiteImage(cv2.imread("test_images/white.png")))

    def test_black(self):
        self.assertFalse(isWhiteImage(cv2.imread("test_images/black.png")))


if __name__ == '__main__':
    unittest.main()
