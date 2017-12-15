""" Code for Day 12 of Advent of Code """

import unittest

def advent_12a(file_name):
    """ Full solution to advent 12a """
    with open(file_name) as input_file:
        pipes = parse([line.strip() for line in input_file.readlines()])
        comp_map, _ = make_component_map(pipes)
        return len(comp_map[0])

def advent_12b(file_name):
    """ Full solution to advent 12a """
    with open(file_name) as input_file:
        pipes = parse([line.strip() for line in input_file.readlines()])
        _, reps = make_component_map(pipes)

        num_components = 0
        for elt, rep in reps.items():
            if elt == rep:
                num_components += 1
        
        return num_components


def parse(lines):
    """ Parses the input lines according to the spec """
    output = dict()

    for line in lines:
        [start, pipes] = line.split("<->")
        output[int(start)] = [int(pipe) for pipe in pipes.split(",")]

    return output

def make_component_map(pipes):
    """ Determines the map of components from all nodes to all other nodes """
    component_representatives = dict()
    components = dict()

    for start in pipes:
        components[start] = {start}
        component_representatives[start] = start

    for start, connections in pipes.items():
        for connection in connections:
            if component_representatives[start] == component_representatives[connection]:
                continue

            to_receive = component_representatives[start]
            to_give = component_representatives[connection]

            for c in components[to_give]:
                components[to_receive].add(c)
                components[c] = components[to_receive]
                component_representatives[c] = to_receive

    return components, component_representatives


class Advent12Tests(unittest.TestCase):
    """ Tests for this day """

    def test_12a(self):
        """ Test the main 12a method """
        actual = advent_12a("fixtures/aoc_12a_test.txt")
        expected = 6
        self.assertEqual(actual, expected)

    def test_12b(self):
        """ Test the main 12b method """
        actual = advent_12b("fixtures/aoc_12a_test.txt")
        expected = 2
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
