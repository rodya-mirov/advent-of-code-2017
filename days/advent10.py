""" Code for Advent of Code Day 10 """
import unittest

def advent_10a(file_name):
    """ Get the product of the first two numbers in the list after twisting, including file IO """
    with open(file_name) as input_file:
        list_length = int(input_file.readline())
        list_to_process = [x for x in range(0, list_length)]
        input_lengths = [int(x) for x in input_file.readline().split(',')]

        twist(list_to_process, input_lengths)

        return list_to_process[0] * list_to_process[1]

def advent_10b(file_name):
    """ Convert  """
    with open(file_name) as input_file:
        list_length = int(input_file.readline())
        list_to_process = [x for x in range(0, list_length)]
        input_lengths = [int(x) for x in input_file.readline().split(',')]

        twist(list_to_process, input_lengths)

        return list_to_process[0] * list_to_process[1]

def twist(list_to_process, input_length_list):
    """ Perform the knot twisting action on the specified list """
    curr_index = 0
    skip_size = 0

    for input_length in input_length_list:
        sub_twist(list_to_process, curr_index, input_length)
        curr_index = (curr_index + input_length + skip_size) % len(list_to_process)
        skip_size += 1

def sub_twist(to_twist, start_index, twist_length):
    """ Twist the list from start_index to start_index + twist_length (modularized) """
    for offset in range(0, twist_length//2):
        left = (start_index + offset) % len(to_twist)
        right = (start_index + twist_length - 1 - offset) % len(to_twist)

        to_twist[left], to_twist[right] = to_twist[right], to_twist[left]

class Advent10Tests(unittest.TestCase):
    """ Tests for this day of code """

    def test_10a_full(self):
        """ Test the full path for 10a, including file IO """
        actual = advent_10a("fixtures/aoc_10a_test.txt")
        expected = 12
        self.assertEqual(actual, expected)

    def test_sub_twist(self):
        """ Test the 'subtwist' function """
        fixtures = [
            ([0, 1, 2, 3, 4], 2, 3, [0, 1, 4, 3, 2]),
            ([0, 1, 2, 3, 4], 4, 3, [0, 4, 2, 3, 1]),
            ([0, 1, 2, 3, 4], 2, 2, [0, 1, 3, 2, 4]),
            ([0, 1, 2, 3, 4], 4, 2, [4, 1, 2, 3, 0]),
            ([0, 1, 2, 3], 1, 3, [0, 3, 2, 1]),
            ([0, 1, 2, 3], 1, 2, [0, 2, 1, 3]),
            ([0, 1, 2, 3], 3, 3, [0, 3, 2, 1]),
            ([0, 1, 2, 3], 3, 2, [3, 1, 2, 0])
        ]

        for start_list, start_index, twist_length, result in fixtures:
            arg_copy = [x for x in start_list]
            sub_twist(start_list, start_index, twist_length)

            message = "Subtwist with list: {}, ind: {}, len: {}".format(
                arg_copy, start_index, twist_length)
            self.assertEqual(start_list, result, msg=message)

if __name__ == '__main__':
    unittest.main()
