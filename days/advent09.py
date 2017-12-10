""" Code for Advent of Code Day 7 """
import unittest

def advent_9a(file_name):
    """ Get the total group score for the input file """
    with open(file_name) as input_file:
        line = input_file.readline()
        group_scores = []
        get_group(line, 0, 1, group_scores, [])
        return sum([value for (_, value) in group_scores])

def advent_9b(file_name):
    """ Get the total garbage score for the input file """
    with open(file_name) as input_file:
        line = input_file.readline()
        garbage_chars = []
        get_group(line, 0, 1, [], garbage_chars)
        return len(garbage_chars)

def get_group(chars, index, current_depth, scores, garbage_chars):
    """ Gets the current group, which is assumed the start at index """
    curr_index = index
    group_string = ""
    finished = True
    exclamation_active = False

    if chars[curr_index] == '{':
        finished = False
        curr_index += 1
        group_string += '{'

    while not finished:
        if curr_index >= len(chars):
            raise Exception("Unexpected EOF when processing group!")

        next_char = chars[curr_index]

        if exclamation_active:
            exclamation_active = False
        elif next_char == '!':
            exclamation_active = True
        elif next_char == '}':
            finished = True
        elif next_char == '{':
            group, curr_index = get_group(chars, curr_index, current_depth + 1, scores, garbage_chars)
            group_string += group
            continue
        elif next_char == '<':
            garbage, curr_index = get_garbage(chars, curr_index, garbage_chars)
            group_string += garbage
            continue

        group_string += next_char
        curr_index += 1

    scores.append((group_string, current_depth))
    return group_string, curr_index

def get_garbage(chars, index, garbage_chars):
    """ Gets the garbage content of the characters, starting at index """
    curr_index = index
    garbage_string = ""
    exclamation_active = False
    finished = True

    if chars[curr_index] == '<':
        finished = False
        garbage_string += '<'
        curr_index += 1

    while not finished:
        if curr_index >= len(chars):
            raise Exception("Unexpected EOF when processing garbage!")

        next_char = chars[curr_index]

        if exclamation_active:
            exclamation_active = False
        elif next_char == '>':
            finished = True
        elif next_char == '!':
            exclamation_active = True
        else:
            garbage_chars.append(next_char)

        garbage_string += next_char

        curr_index += 1

    return garbage_string, curr_index

class Advent9Tests(unittest.TestCase):
    """ Tests for this day of code """

    def test_get_garbage(self):
        """ Tests the 'get garbage' functionality """
        tests = {
            '<>': ('<>', 2, ''),
            '<random characters>': ('<random characters>', 19, 'random characters'),
            '<<<>': ('<<<>', 4, '<<'),
            '<!>>': ('<!>>', 4, ''),
            '<!>>>>': ('<!>>', 4, ''),
            '<{!>}>': ('<{!>}>', 6, '{}'),
            '<!!>': ('<!!>', 4, ''),
            '<!!!>>': ('<!!!>>', 6, ''),
            '<{o"i!a,<{i<a>': ('<{o"i!a,<{i<a>', 14, '{o"i,<{i<a'),
            '<<!>>,<!!>': ('<<!>>', 5, '<')
        }

        for args, answers in tests.items():
            message = "Input was '{}'".format(args)
            garbage_chars = []
            actual_garbage, actual_index = get_garbage(args, 0, garbage_chars)

            expected_garbage = answers[0]
            expected_index = answers[1]
            expected_garbage_str = answers[2]

            actual_garbage_str = ''
            for c in garbage_chars:
                actual_garbage_str += c

            self.assertEqual(actual_garbage, expected_garbage, msg=("Garbage: " + message))
            self.assertEqual(actual_index, expected_index, msg=("Index: " + message))
            self.assertEqual(actual_garbage_str, expected_garbage_str, msg=("Garbage str: " + message))

    def test_get_group(self):
        """ Test the 'get group' logic """
        tests = {
            '{}': ('{}', 2, 1, 1, ''),
            '{random characters}': ('{random characters}', 19, 1, 1, ''),
            '{<<>}': ('{<<>}', 5, 1, 1, '<'),
            '{!}}': ('{!}}', 4, 1, 1, ''),
            '{}{}': ('{}', 2, 1, 1, ''),
            '{{}}': ('{{}}', 4, 2, 3, ''),
            '{<<!<>{<asbd>}<ds>}': ('{<<!<>{<asbd>}<ds>}', 19, 2, 3, '<asbdds')
        }

        for args, answers in tests.items():
            groups = []
            garbage_chars = []

            message = "Input was '{}'".format(args)
            actual_group, actual_index = get_group(args, 0, 1, groups, garbage_chars)
            actual_num_gps = len(groups)
            actual_total_score = sum([score for (group, score) in groups])

            actual_garbage_str = ''
            for c in garbage_chars:
                actual_garbage_str += c

            expected_group, expected_index, expected_num_groups, expected_total_score, expected_garbage_str = answers


            self.assertEqual(actual_group, expected_group, msg=("Main group: " + message))
            self.assertEqual(actual_index, expected_index, msg=("End index: " + message))
            self.assertEqual(actual_num_gps, expected_num_groups, msg=("Num groups: " + message))
            self.assertEqual(actual_total_score, expected_total_score, msg=("Total score: " + message))
            self.assertEqual(actual_garbage_str, expected_garbage_str, msg=("Garbage str: " + message))


if __name__ == '__main__':
    unittest.main()
