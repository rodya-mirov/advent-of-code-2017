""" Code for Advent of Code Day 7 """
import unittest

def advent_8a(input_filename):
    """ Parse and execute the code for 8a """
    with open(input_filename) as input_file:
        instructions = [parse(line) for line in input_file.readlines()]
        state = dict()

        for instruction in instructions:
            instruction.execute(state)

        return max(state.values())

def advent_8b(input_filename):
    """ Parse and execute the code for 8a """
    with open(input_filename) as input_file:
        instructions = [parse(line) for line in input_file.readlines()]
        state = dict()

        max_val = 0
        for instruction in instructions:
            instruction.execute(state)
            max_val = max(max_val, state.get(instruction.register_name, 0))

        return max_val

class Instruction:
    """ Class representing a complete instruction """
    def __init__(self, register_name, increment, condition):
        self.register_name = register_name
        self.increment = increment
        self.condition = condition

    def execute(self, state):
        """ Execute this instruction against the given state """
        if self.condition.check(state):
            old_val = state.get(self.register_name, 0)
            new_val = old_val + self.increment
            state[self.register_name] = new_val

class Condition:
    """ Class representing a condition as part of an Instruction"""
    def __init__(self, register_name, operator, value):
        self.register_name = register_name

        if operator == '>':
            self.checker = (lambda x: x > value)
        elif operator == '<':
            self.checker = (lambda x: x < value)
        elif operator == '>=':
            self.checker = (lambda x: x >= value)
        elif operator == '<=':
            self.checker = (lambda x: x <= value)
        elif operator == '==':
            self.checker = (lambda x: x == value)
        elif operator == '!=':
            self.checker = (lambda x: x != value)
        else:
            raise Exception("Unrecognized operator '{}'".format(operator))

    def check(self, state):
        """ Check if this condition is 'true' for this state """
        val = state.get(self.register_name, 0)
        return self.checker(val)

def parse(line):
    """ Parse a line of input as an instruction """
    tokens = line.split()
    if len(tokens) != 7 or tokens[3] != 'if':
        raise Exception("Cannot parse line '{}'".format(line))

    register_name = tokens[0]

    if tokens[1] == 'inc':
        increment = int(tokens[2])
    elif tokens[1] == 'dec':
        increment = -int(tokens[2])
    else:
        raise Exception("Unknown incrementer '{}' in line '{}'".format(tokens[1], line))

    cond_register_name = tokens[4]
    operator = tokens[5]
    operator_value = int(tokens[6])

    condition = Condition(cond_register_name, operator, operator_value)
    return Instruction(register_name, increment, condition)

class Advent8Tests(unittest.TestCase):
    """ Tests for this day of code """

    def test_8a(self):
        """ Test the main 'whole path' method for 8a """
        actual = advent_8a('aoc_8_test.txt')
        expected = 1
        self.assertEqual(actual, expected)

    def test_8b(self):
        """ Test the main 'whole path' method for 8b """
        actual = advent_8b('aoc_8_test.txt')
        expected = 10
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
