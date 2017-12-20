""" Code supporting day 13 of advent of code, 2017 """

import unittest

def advent_13a(file_name):
    """ Whole path for 13a """
    with open(file_name) as input_file:
        design = parse(input_file.readlines())
        return severity(design)

def advent_13b(file_name):
    """ Whole path for 13b """
    with open(file_name) as input_file:
        design = parse(input_file.readlines())

        increment = 1
        if (1, 2) in design:
            increment = 2 # (1, 2) prevents odd delays from ever working

        delay = 0
        while not can_pass(delay, design):
            delay += increment

        return delay

def parse(lines):
    """ Parse the specified input into a list of pairs """
    def parse_line(line):
        """ Parse a single line """
        [depth, patrol_length] = line.split(":")
        return (int(depth), int(patrol_length))

    return [parse_line(line) for line in lines]

def severity(design):
    """ Determine the severity of getting caught when starting on the first ps """
    return sum([subseverity(depth, patrol_length) for (depth, patrol_length) in design])

def subseverity(depth, patrol_length):
    """ Determine the severity (if any) of getting caught (if getting caught) """
    if pos_at_time(depth, patrol_length) == 0:
        return depth * patrol_length
    else:
        return 0

def can_pass(delay, design):
    """ Determine if the specified delay gets through the design OK """
    for (depth, patrol_length) in design:
        time = depth + delay
        if pos_at_time(time, patrol_length) == 0:
            return False

    return True

def pos_at_time(time, patrol_length):
    """ Determine the position the scanner will be at, at the particular time """
    if patrol_length == 1:
        return 0

    period = patrol_length * 2 - 2 # e.g.: 3 -> 0, 1, 2, 1, (0, 1, 2, 1, 0, 1, 2, 1, ...)
    pos = time % period
    if pos >= patrol_length:
        pos = period - pos

    return pos


class Advent13Test(unittest.TestCase):
    """ Test this functionality! """

    def test_13a(self):
        """ Test 13a with a fixture """
        expected = 24
        actual = advent_13a("fixtures/aoc_13a_test.txt")
        self.assertEqual(actual, expected)

    def test_13b(self):
        """ Test 13b with a fixture """
        expected = 10
        actual = advent_13b("fixtures/aoc_13a_test.txt")
        self.assertEqual(actual, expected)

    def test_pos_at_time(self):
        """ Some hard-coded tests of 'pos_at_time' """
        self.assertEqual(pos_at_time(1, 2), 1, msg="Args: 1, 2")
        self.assertEqual(pos_at_time(0, 4), 0, msg="Args: 0, 4")
        self.assertEqual(pos_at_time(1, 4), 1, msg="Args: 1, 4")
        self.assertEqual(pos_at_time(2, 4), 2, msg="Args: 2, 4")
        self.assertEqual(pos_at_time(3, 4), 3, msg="Args: 3, 4")
        self.assertEqual(pos_at_time(4, 4), 2, msg="Args: 4, 4")
        self.assertEqual(pos_at_time(5, 4), 1, msg="Args: 5, 4")
        self.assertEqual(pos_at_time(6, 4), 0, msg="Args: 6, 4")
        self.assertEqual(pos_at_time(7, 4), 1, msg="Args: 7, 4")
        self.assertEqual(pos_at_time(6, 4), 0, msg="Args: 6, 4")

    def test_subseverity(self):
        """ Test the actually important method """
        known = {
            (0, 1): 0,
            (0, 10): 0,
            (1, 1): 1,
            (1, 2): 0,
            (1, 30): 0,
            (2, 1): 2,
            (2, 2): 4,
            (2, 3): 0,
            (2, 10): 0,
            (3, 1): 3,
            (3, 2): 0,
            (3, 3): 0,
            (11, 1): 11,
            (11, 20): 0,
            (12, 1): 12,
            (12, 2): 24,
            (12, 3): 36,
            (12, 4): 48,
            (12, 5): 0,
            (12, 6): 0,
            (12, 7): 12*7,
            (12, 12): 0
        }

        for (depth, patrol_length), expected in known.items():
            actual = subseverity(depth, patrol_length)
            message = "Input was ({}, {})".format(depth, patrol_length)
            self.assertEqual(expected, actual, msg=message)

if __name__ == '__main__':
    unittest.main()
