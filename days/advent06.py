""" Code for Advent of Code, Day 6 """
import unittest

def advent_6a(input_string):
    """ Solve advent problem 6a """
    initial = [int(x) for x in input_string.split()]
    return num_steps(initial)

def advent_6b(input_string):
    """ Solve advent problem 6b """
    initial = [int(x) for x in input_string.split()]
    return cycle_length(initial)

def num_steps(block_state):
    """ Determine the number of steps required to find a repeated state """
    seen = set()
    state_tuple = tuple(block_state)
    iterations = 0

    while state_tuple not in seen:
        seen.add(state_tuple)
        iterations += 1
        progress(block_state)
        state_tuple = tuple(block_state)

    return iterations

def cycle_length(block_state):
    """ Determine the number of steps required to find a repeated state """
    seen = set()
    seen_list = list()
    state_tuple = tuple(block_state)

    while state_tuple not in seen:
        seen.add(state_tuple)
        seen_list.append(state_tuple)
        progress(block_state)
        state_tuple = tuple(block_state)

    # Now we're in an infinite loop ...
    for i in range(0, len(seen_list)):
        if seen_list[i] == state_tuple:
            return len(seen_list) - i

def progress(block_state):
    """ Progress the block state one timestep """
    if not block_state:
        return

    array_length = len(block_state)

    # First, find the maximum index and value
    max_val = block_state[0]
    max_ind = 0

    for ind in range(1, array_length):
        val = block_state[ind]
        if val > max_val:
            max_val = val
            max_ind = ind

    # Then communism
    block_state[max_ind] = 0
    remaining = max_val
    index = (max_ind + 1) % array_length
    while remaining > 0:
        block_state[index] += 1
        remaining -= 1
        index = (index + 1) % array_length


class Advent6Tests(unittest.TestCase):
    """ Unit tests for the functions in this module """

    def test_progress(self):
        """ Test that the 'progress' method works """
        known = {
            (0, 2, 7, 0): (2, 4, 1, 2),
            (2, 4, 1, 2): (3, 1, 2, 3),
            (3, 1, 2, 3): (0, 2, 3, 4),
            (0, 2, 3, 4): (1, 3, 4, 1),
            (1, 3, 4, 1): (2, 4, 1, 2)
        }

        for arg, expected in known.items():
            block = list(arg)
            progress(block)
            actual = tuple(block)
            self.assertEqual(actual, expected, msg=("Input: {}".format(arg)))

    def test_num_steps(self):
        """ Test that the 'num_steps' method works """
        known = {
            (0, 2, 7, 0): 5,
            (2, 4, 1, 2): 4,
            (3, 1, 2, 3): 4,
            (0, 2, 3, 4): 4,
            (1, 3, 4, 1): 4
        }

        for arg, expected in known.items():
            block = list(arg)
            actual = num_steps(block)
            self.assertEqual(actual, expected, msg=("Input: {}".format(arg)))

    def test_cycle_length(self):
        """ Test that the 'num_steps' method works """
        known = {
            (0, 2, 7, 0): 4,
            (2, 4, 1, 2): 4,
            (3, 1, 2, 3): 4,
            (0, 2, 3, 4): 4,
            (1, 3, 4, 1): 4
        }

        for arg, expected in known.items():
            block = list(arg)
            actual = cycle_length(block)
            self.assertEqual(actual, expected, msg=("Input: {}".format(arg)))

if __name__ == '__main__':
    unittest.main()
