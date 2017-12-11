""" Code supporting day 4 of advent of code """

import unittest

def parse_file(file_name):
    """ Parse the file to a list of integers """
    with open(file_name) as input_file:
        return [int(token) for token in input_file.readlines() if token]

def count_jumps_5a(steps):
    """ Determine the total number of jumps required to exit the maze """
    index = 0
    jumps = 0

    while index >= 0 and index < len(steps):
        jumps += 1
        next_jump = steps[index]
        steps[index] += 1
        index += next_jump

    return jumps

def advent_5a(file_name):
    """ Solve the puzzle specified by the filename """
    steps = parse_file(file_name)
    return count_jumps_5a(steps)

def count_jumps_5b(steps):
    """ Determine the total number of jumps required to exit the maze """
    index = 0
    jumps = 0

    while index >= 0 and index < len(steps):
        jumps += 1
        next_jump = steps[index]
        if next_jump >= 3:
            steps[index] -= 1
        else:
            steps[index] += 1
        index += next_jump

    return jumps

def advent_5b(file_name):
    """ Solve the puzzle specified by the filename """
    steps = parse_file(file_name)
    return count_jumps_5b(steps)

class Advent5Tests(unittest.TestCase):
    """ Unit tests for the functions in this module """

    def test_count_jumps_5a(self):
        """ Test the 'count_jumps_5a' helper method """
        actual = count_jumps_5a([0, 3, 0, 1, -3])
        expected = 5
        self.assertEqual(actual, expected)

    def test_count_jumps_5b(self):
        """ Test the 'count_jumps_5b' helper method """
        actual = count_jumps_5b([0, 3, 0, 1, -3])
        expected = 10
        self.assertEqual(actual, expected)

    def test_5a_full_test(self):
        """ Test the whole path for 5a, including file io """
        actual = advent_5a("fixtures/aoc_5a_test.txt")
        expected = 5
        self.assertEqual(actual, expected)

    def test_5b_full_test(self):
        """ Test the whole path for 5b, including file io """
        actual = advent_5b("fixtures/aoc_5a_test.txt")
        expected = 10
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
