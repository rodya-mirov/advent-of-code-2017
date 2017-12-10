""" Code for Advent of Code Day 7 """
import unittest

def advent_7a(input_filename):
    """ Including filo IO, solve advent 7a """
    with open(input_filename) as input_file:
        nodes = [parse(row) for row in input_file.readlines()]
        return find_root(nodes)

def advent_7b(input_filename):
    """ Including file IO, solve 7b """
    with open(input_filename) as input_file:
        nodes = [parse(row) for row in input_file.readlines()]
        tree = build_tree(nodes)
        _, corrected_weight = wrong_node(tree)
        return corrected_weight

class Node:
    """ Data structure representing a node """
    def __init__(self, name, weight, children):
        """ Create a Node from a string representation of that node """
        self.name = name
        self.weight = weight
        self.children = children

    def __eq__(self, other):
        """ Equality based on fields """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ Yes this is not redundant, yay Python """
        return not (self == other)

def parse(line):
    """ Parse a string line into a Node """
    tokens = line.split()
    if len(tokens) < 2 or len(tokens) == 3:
        raise Exception("Could not parse Node: '{}'".format(line))

    name = tokens[0]
    weight = int(tokens[1][1:-1])

    if len(tokens) == 2:
        children = []
    else:
        children = []
        for i in range(3, len(tokens)-1):
            children.append(tokens[i][:-1]) # drop the trailing comma

        children.append(tokens[-1]) # no trailing comma at the end

    return Node(name, weight, children)

def find_root(nodes):
    """ Find the name of the root program in the architecture """
    all_children = set()
    possible_roots = set()

    for node in nodes:
        all_children.update(node.children)
        possible_roots.add(node.name)

    for child in all_children:
        possible_roots.remove(child)

    if len(possible_roots) != 1:
        raise Exception("Had {} possible roots, expected 1".format(len(possible_roots)))

    return possible_roots.pop()

def build_tree(nodes):
    """ Builds a tree from the list of nodes. This is destructive to the data in nodes. """
    root_name = find_root(nodes)

    # First build a lookup table name -> node
    all_nodes = dict()

    for node in nodes:
        all_nodes[node.name] = node

    # Then replace names with actual references in the nodes ...
    for node in nodes:
        node.children = [all_nodes[child_name] for child_name in node.children]

    root = all_nodes[root_name]

    # Then assign the true weights
    assign_weights(root)

    return root

def assign_weights(node):
    """ Recursively assign 'true weights' to nodes in a tree """
    children_weight = 0
    if node.children:
        for child in node.children:
            assign_weights(child)
            children_weight += child.true_weight

    node.true_weight = node.weight + children_weight

def wrong_node(root):
    """
    Finds the wrong node in the tree hierarchy, deeply.

    A node can only be wrong if it has siblings and all but one agree!

    Return is (node with issue, corrected weight)
    """

    # If no children, stop
    if not root.children:
        return None, 0

    # Then check if the problem is below you
    for child in root.children:
        bad_node, fixed_weight = wrong_node(child)
        if bad_node:
            return bad_node, fixed_weight

    # Otherwise the problem could be among your children ...
    if len(root.children) > 2:
        weight_counts = dict()
        for child in root.children:
            mult = weight_counts.get(child.true_weight, 0)
            weight_counts[child.true_weight] = mult+1

        # If we found a discrepancy ...
        if len(weight_counts) > 1:
            # Then find the bad child and figure out what it should have been
            for child in root.children:
                if weight_counts[child.true_weight] == 1:
                    bad_node = child
                    weight_counts.pop(child.true_weight)
                    better_true_weight = next(iter(weight_counts.keys()))
                    correction = better_true_weight - bad_node.true_weight
                    corrected_weight = bad_node.weight + correction
                    return bad_node, corrected_weight

    # If we got this far our children are balanced
    return None, 0

class Advent7Tests(unittest.TestCase):
    """ Tests for this day of code """

    def test_7a(self):
        """ Test the main 'whole path' method for 7a """
        actual = advent_7a('aoc_7a_test.txt')
        expected = 'tknk'
        self.assertEqual(actual, expected)

    def test_parse(self):
        """ Test the 'parse' method for 7a """
        known = {
            'wdysq (135) -> sxldvex, wiasj': Node('wdysq', 135, ['sxldvex', 'wiasj']),
            'vjwuuft (33) -> inuci, neddz, rwamq': Node('vjwuuft', 33, ['inuci', 'neddz', 'rwamq']),
            'oislgqy (77)': Node('oislgqy', 77, [])
        }

        for argument, expected in known.items():
            actual = parse(argument)
            if actual != expected:
                print(argument, actual.__dict__, expected.__dict__)
            self.assertEqual(actual, expected, msg=argument)

if __name__ == '__main__':
    unittest.main()
