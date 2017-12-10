""" Code for Advent of Code, Day 3 """

import unittest
import itertools

def advent_3b(cap):
    """ Finds the first iterated number greater than cap """
    for x in iter_nums():
        if x > cap:
            return x

def iter_nums():
    """ Iterates through all generated numbers in order """
    saved = dict()

    def get_or_zero(x, y):
        """ Get the value at (x, y) in the cache, or return 0 """
        coord = (x, y)
        if coord in saved:
            return saved[coord]
        else:
            return 0

    for coord in iter_coords():
        x, y = coord
        if coord == (0, 0):
            val = 1
        else:
            val = 0
            val += get_or_zero(x-1, y-1)
            val += get_or_zero(x, y-1)
            val += get_or_zero(x+1, y-1)
            val += get_or_zero(x-1, y)
            val += get_or_zero(x+1, y)
            val += get_or_zero(x-1, y+1)
            val += get_or_zero(x, y+1)
            val += get_or_zero(x+1, y+1)

        saved[coord] = val

        yield val

def iter_coords():
    """ Defines a generator which goes through and outputs all coordinates in order """
    yield (0, 0)
    incr = 0
    x = 1
    y = 0

    while True:
        incr += 2

        top = y + incr - 1
        bot = y - 1
        left = x - incr
        right = x

        yield (x, y)
        while y < top:
            y += 1
            yield (x, y)

        while x > left:
            x -= 1
            yield (x, y)

        while y > bot:
            y -= 1
            yield (x, y)

        while x < right:
            x += 1
            yield (x, y)

        x += 1


def advent_3a(num):
    """ Determine the cost of moving num back to the origin """
    x, y = coords_3a(num)
    return abs(x) + abs(y)

def coords_3a(num):
    """ Determine the coordinates (x, y) of the specified number """
    if num == 1:
        return (0, 0)

    less = 1
    less_pos = (0, 0)
    more = 1
    more_pos = (0, 0)
    incr = 0

    while more < num:
        incr += 2
        less = more + 1
        less_pos = (more_pos[0]+1, more_pos[1]) # shift to the right one place

        more += 4 * incr
        more_pos = (more_pos[0]+1, more_pos[1]-1) # shift down+right one place

    upper_right = less + incr - 1
    upper_left = upper_right + incr
    lower_left = upper_left  + incr

    if num <= upper_right:
        x = less_pos[0]
        y = less_pos[1] + (num - less)
        return (x, y)
    elif num <= upper_left:
        x = less_pos[0] - (num - upper_right)
        y = less_pos[1] + (incr - 1)
        return (x, y)
    elif num <= lower_left:
        x = less_pos[0] - incr
        y = more_pos[1] + incr - (num - upper_left)
        return (x, y)
    else:
        x = less_pos[0] - incr + (num - lower_left)
        y = more_pos[1]
        return (x, y)

class Advent3Tests(unittest.TestCase):
    """ Unit tests for the functions in this module """

    def test_3a(self):
        """ Test the 3a code against the given test cases """
        known_values = {
            1: 0,
            12: 3,
            23: 2,
            1024: 31
        }

        for number, expected in known_values.items():
            actual = advent_3a(number)
            message = ("Testing input '{}', expected '{}' but got '{}'"
                       .format(number, expected, actual))
            self.assertEqual(advent_3a(number), expected, msg=message)
    
    def test_3b(self):
        known_values = {
            0: 1,
            1: 2,
            2: 4,
            37: 54,
            100: 122
        }

        for number, expected in known_values.items():
            actual = advent_3b(number)
            message = ("Testing input '{}', expected '{}' but got '{}'"
                       .format(number, expected, actual))
            self.assertEqual(actual, expected, msg=message)

    def test_get_coords(self):
        """ Check all the known values for coordinates to see if the function works """
        known_values = {
            1: (0, 0),
            2: (1, 0),
            3: (1, 1),
            4: (0, 1),
            5: (-1, 1),
            6: (-1, 0),
            7: (-1, -1),
            8: (0, -1),
            9: (1, -1),
            10: (2, -1),
            11: (2, 0),
            12: (2, 1),
            13: (2, 2),
            14: (1, 2),
            15: (0, 2),
            16: (-1, 2),
            17: (-2, 2),
            18: (-2, 1),
            19: (-2, 0),
            20: (-2, -1),
            21: (-2, -2),
            22: (-1, -2),
            23: (0, -2),
            24: (1, -2),
            25: (2, -2),
            26: (3, -2),
        }

        for number, expected in known_values.items():
            actual = coords_3a(number)
            message = ("Testing input '{}', expected '{}' but got '{}'"
                       .format(number, expected, actual))
            self.assertEqual(actual, expected, msg=message)
    
    def test_traversal(self):
        """ Test we're traversing things in the right order """
        expected = [
            (0, 0),
            (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1),
            (2, -1), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (-1, 2), (-2, 2),
            (-2, 1), (-2, 0), (-2, -1), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2),
            (3, -2)
        ]

        num_desired = len(expected)
        actual = list(itertools.islice(iter_coords(), num_desired))

        for i in range(0, num_desired):
            message = "At index '{}', expected '{}' and got '{}'".format(i, expected[0], actual[0])
            self.assertEqual(expected[i], actual[i], msg=message)

if __name__ == '__main__':
    unittest.main()
