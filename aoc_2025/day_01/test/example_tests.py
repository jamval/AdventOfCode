import os
import unittest
from aoc_2025.day_01.src.day01_common import solve_puzzle01, generate_example_input
from common.input_support import get_examples_path


class Day01ExampleTests(unittest.TestCase):
    def test_puzzle01_example(self):
        # Arrange
        file_path = generate_example_input()
        expected = 3

        # Act
        actual = solve_puzzle01(file_path)

        # Assert
        self.assertEqual(expected, actual)  # add assertion here

    def test_puzzle02_example(self):
        # Arrange
        file_path = generate_example_input()
        expected = 3

        # Act
        actual = solve_puzzle02(file_path)

        # Assert
        self.assertEqual(expected, actual)  # add assertion here

if __name__ == '__main__':
    unittest.main()