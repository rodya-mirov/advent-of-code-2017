""" Do Advent of Code 2017, Day 11 """
import unittest

def advent_11a(file_name):
    """ Do the full flow for day 11a """
    with open(file_name) as input_file:
        steps = [token for token in input_file.readline().strip().split(',')]
        return distance_to_origin(steps)

def advent_11b(file_name):
    """ Do the full flow for day 11b """
    with open(file_name) as input_file:
        steps = [token for token in input_file.readline().strip().split(',')]
        return max_distance_to_origin(steps)

def distance_to_origin_from_coords(n_counter, ne_counter, se_counter):
    """ Determine the distance to the origin from the coordinates """
    # Finally, there are a couple relations which reduce the total:
    #    N  + SE == NE
    #    NW + NE == N  (that is, NE - SE == N)
    #    S  + NE == SE (that is, NE - N == SE)
    # All these moves reduce the total absolute value |N| + |SE| + |NE| so the loop must terminate
    found = True
    while found:
        found = False

        # apply:   N + SE => NE
        if n_counter > 0 and se_counter > 0:
            amount = min(n_counter, se_counter)
            found = True
            n_counter -= amount
            se_counter -= amount
            ne_counter += amount

        # apply:  -N - SE => -NE
        if n_counter < 0 and se_counter < 0:
            amount = min(-n_counter, -se_counter)
            found = True
            n_counter += amount
            se_counter += amount
            ne_counter -= amount

        # apply:  NE - SE => N
        if se_counter < 0 and ne_counter > 0:
            amount = min(-se_counter, ne_counter)
            found = True
            n_counter += amount
            ne_counter -= amount
            se_counter += amount

        # apply: -NE + SE => -N
        if se_counter > 0 and ne_counter < 0:
            amount = min(se_counter, -ne_counter)
            found = True
            se_counter -= amount
            ne_counter += amount
            n_counter -= amount

        # apply:  -N + NE => SE
        if n_counter < 0 and ne_counter > 0:
            amount = min(-n_counter, ne_counter)
            found = True
            n_counter += amount
            ne_counter -= amount
            se_counter += amount

        # apply:   N - NE => -SE
        if n_counter > 0 and ne_counter < 0:
            amount = min(n_counter, -ne_counter)
            found = True
            n_counter -= amount
            ne_counter += amount
            se_counter -= amount

    # The counters are now minimally represented, so this is a minimal path home :)
    return abs(n_counter) + abs(ne_counter) + abs(se_counter)

def max_distance_to_origin(steps):
    """ Determine the maximum distance to the origin ever during the path """
    # The motion is commutative, so only counts, not order, matters.
    # Also, NE/SW, N/S, and SE/NW all cancel, so there are only three counters.
    ne_counter = 0
    se_counter = 0
    n_counter = 0

    most_distance = 0

    for step in steps:
        if step == 'ne':
            ne_counter += 1
        elif step == 'n':
            n_counter += 1
        elif step == 's':
            n_counter -= 1
        elif step == 'se':
            se_counter += 1
        elif step == 'sw':
            ne_counter -= 1
        elif step == 'nw':
            se_counter -= 1
        else:
            raise Exception("Unrecognized direction '{}'".format(step))

        curr_distance = distance_to_origin_from_coords(n_counter, ne_counter, se_counter)
        most_distance = max(most_distance, curr_distance)

    return most_distance

def distance_to_origin(steps):
    """ Determine the distance to the origin given that the steps were already taken """
    # The motion is commutative, so only counts, not order, matters.
    # Also, NE/SW, N/S, and SE/NW all cancel, so there are only three counters.
    ne_counter = 0
    se_counter = 0
    n_counter = 0

    for step in steps:
        if step == 'ne':
            ne_counter += 1
        elif step == 'n':
            n_counter += 1
        elif step == 's':
            n_counter -= 1
        elif step == 'se':
            se_counter += 1
        elif step == 'sw':
            ne_counter -= 1
        elif step == 'nw':
            se_counter -= 1
        else:
            raise Exception("Unrecognized direction '{}'".format(step))

    return distance_to_origin_from_coords(n_counter, ne_counter, se_counter)


class Advent11Test(unittest.TestCase):
    """ Tests for this module """

    # The other methods are trivial variations on this so one test is really fine
    def test_distance_to_origin(self):
        """ Test the distance to origin method """
        known = [
            (['ne', 'ne', 'ne'], 3),
            (['ne', 'ne', 'sw', 'sw'], 0),
            (['ne', 'ne', 's', 's'], 2),
            (['se', 'sw', 'se', 'sw', 'sw'], 3)
        ]

        for steps, expected in known:
            message = "Input was '{}'".format(steps)
            actual = distance_to_origin(steps)
            self.assertEqual(actual, expected, msg=message)

if __name__ == '__main__':
    unittest.main()
