# Class 20
import unittest

def is_symmetric(matrix) -> bool:
    lines = len(matrix)
    columns = len(matrix[0]) # Same amount of lines and columns

    # m[i][j] == m[j][i]
    for i in range(lines):
        # Starts in position 1 because we're checking the upper diagonal
        for j in range(i + 1, columns):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

class TestIsSymmetricFunction(unittest.TestCase):
    def test_is_symmetric(self):
        self.assertTrue(is_symmetric([[1,2,3], [2,4,5], [3,5,2]]))
    def test_is_not_symmetric(self):
        self.assertFalse(is_symmetric([[1,2,2], [2,4,5], [3,5,2]]))
