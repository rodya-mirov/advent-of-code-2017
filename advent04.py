""" Code supporting day 4 of advent of code """

import unittest

def make_rows(file_name):
    """ Turn a filename into an array of rows, which are arrays of tokens """
    with open(file_name) as input_file:
        return [line.split() for line in input_file.readlines() if line]

def advent_4a(file_name):
    """ Solve puzzle 4a """
    rows = make_rows(file_name)
    total = 0
    for row in rows:
        if is_valid_4a(row):
            total += 1
    return total

def is_valid_4a(row):
    """ Determine if a row is valid by seeing if there are duplicate tokens """
    return len(set(row)) == len(row)

def advent_4b(file_name):
    """ Solve puzzle 4b """
    rows = make_rows(file_name)
    total = 0
    for row in rows:
        if is_valid_4b(row):
            total += 1
    return total

def is_valid_4b(row):
    """ Determine if the row contains any repeated tokens by anagram """
    improved_row = [tuple(sorted(token)) for token in row]

    return len(set(improved_row)) == len(improved_row)

class Advent4Tests(unittest.TestCase):
    """ Unit tests for the functions in this module """

    def test_4a_row_test(self):
        """ Test the 'is_valid(row)' helper method """
        self.assertTrue(is_valid_4a("aa bb cc dd ee".split()))
        self.assertFalse(is_valid_4a("aa bb cc dd aa".split()))
        self.assertTrue(is_valid_4a("aa bb cc dd aaa".split()))

    def test_4a_full_test(self):
        """ Test the whole path for 4a, including file io """
        actual = advent_4a("aoc_4a_test.txt")
        expected = 2
        self.assertEqual(actual, expected)

    def test_4b_row_test(self):
        """ Test is 'is_valid_4b(row)' helper method """
        self.assertTrue(is_valid_4b("abcde fghij".split()))
        self.assertFalse(is_valid_4b("abcde xyz ecdab".split()))
        self.assertTrue(is_valid_4b("a ab abc abd abf abj".split()))
        self.assertTrue(is_valid_4b("iiii oiii ooii oooi oooo".split()))
        self.assertFalse(is_valid_4b("oiii ioii iioi iiio".split()))

    def test_4b_full_test(self):
        """ Test the whole path for 4b """
        actual = advent_4b("aoc_4b_test.txt")
        expected = 3
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
