""" Code to support Day 18 """

import unittest
from queue import Queue

ACCEPTED_TOKENS = {'snd', 'set', 'add', 'mul', 'mod', 'rcv', 'jgz'}

def advent_18a(file_name):
    """ Determine the recovered frequency, if any """
    with open(file_name) as input_file:
        program = parse(input_file.readlines())
        state = dict()
        return received_frequency(program, state, 0)

def advent_18b(file_name):
    """ Determine the number of times P1 sends values """
    with open(file_name) as input_file:
        program = parse(input_file.readlines())
        return duet(program)

def received_frequency(program, state, index):
    """ Execute the program in order to determine the first received frequency """
    received_sound = 0
    while True:
        if index < 0 or index >= len(program):
            return None

        line = program[index]
        cmd = line[0]

        if cmd == 'jgz':
            if line[1](state) > 0:
                index += line[2](state)
                continue

        if cmd == 'snd':
            received_sound = line[1](state)
        elif cmd == 'set':
            state[line[1]] = line[2](state)
        elif cmd == 'add':
            state[line[1]] = state.get(line[1], 0) + line[2](state)
        elif cmd == 'mul':
            state[line[1]] = state.get(line[1], 0) * line[2](state)
        elif cmd == 'mod':
            state[line[1]] = state.get(line[1], 0) % line[2](state)
        elif cmd == 'rcv':
            # ignore value
            if received_sound != 0:
                return received_sound

        index += 1

def duet(program):
    """ Perform a duet; at termination or deadlock output the number of times P1 sends a value """
    p1_sends = 0

    p0_index = 0
    p0_state = {'p': 0}
    p0_rcv_queue = Queue()

    p0_is_waiting = False

    p1_index = 0
    p1_state = {'p': 1}
    p1_rcv_queue = Queue()

    p1_is_waiting = False

    while True:
        if p0_is_waiting and not p0_rcv_queue.empty():
            p0_is_waiting = False

        if p1_is_waiting and not p1_rcv_queue.empty():
            p1_is_waiting = False

        if not(p0_is_waiting or p0_index < 0 or p0_index >= len(program)):
            p0_index, p0_is_waiting = duet_step(program, p0_index, p0_state, p0_rcv_queue, p1_rcv_queue)
        elif not(p1_is_waiting or p1_index < 0 or p1_index >= len(program)):
            old_p1_sends = p0_rcv_queue.qsize()
            p1_index, p1_is_waiting = duet_step(program, p1_index, p1_state, p1_rcv_queue, p0_rcv_queue)
            p1_sends += p0_rcv_queue.qsize() - old_p1_sends
        else:
            return p1_sends

def duet_step(program, instr_index, state, rcv_queue, snd_queue):
    """ Perform a single step of a program; return (index, waiting) and alter state """
    line = program[instr_index]
    cmd = line[0]

    if cmd == 'snd':
        val = line[1](state)
        snd_queue.put(val)
        return (instr_index+1, False)
    elif cmd == 'rcv':
        if rcv_queue.empty():
            return (instr_index, True)
        else:
            val = rcv_queue.get()
            register = line[1]
            state[register] = val
            return (instr_index+1, False)
    elif cmd == 'jgz':
        if line[1](state) > 0:
            return (instr_index + line[2](state), False)

    # Now for the simple ones with shared return logic
    elif cmd == 'set':
        state[line[1]] = line[2](state)
    elif cmd == 'add':
        state[line[1]] = state.get(line[1], 0) + line[2](state)
    elif cmd == 'mul':
        state[line[1]] = state.get(line[1], 0) * line[2](state)
    elif cmd == 'mod':
        state[line[1]] = state.get(line[1], 0) % line[2](state)
    else:
        raise Exception("Unimplemented command: '{}'".format(cmd))

    return (instr_index+1, False)

def is_register(token):
    """ Determine if this is a valid register name """
    return len(token) == 1 and token in "abcdefghijklmnopqrstuvwxyz"

def parse(lines):
    """ Parse an entire program, line by line """
    return [parse_line(line) for line in lines]

def parse_line(line):
    """ Parse a single line of text """
    tokens = line.split()

    def make_eval(token):
        """ Make an evaluation function from the specified token """
        if is_register(token):
            return lambda state: state.get(token, 0)
        else:
            val = int(token)
            return lambda state: val

    if len(tokens) not in {2, 3}:
        raise Exception("All commands have either two or three tokens! Line: '{}'".format(line))

    cmd = tokens[0]
    if cmd not in ACCEPTED_TOKENS:
        raise Exception("Unrecognized command: '{}'".format(cmd))

    if cmd == 'jgz':
        get_x = make_eval(tokens[1])
        get_y = make_eval(tokens[2])

        return [cmd, get_x, get_y]

    if cmd == 'snd':
        get_x = make_eval(tokens[1])
        return [cmd, get_x]

    register = tokens[1]
    if not is_register(register):
        raise Exception("Invalid register name: '{}'".format(register))

    if len(tokens) == 2:
        return [cmd, register]
    else:
        return [cmd, register, make_eval(tokens[2])]

class Advent18Test(unittest.TestCase):
    """ Tests when useful """

    def test_18a(self):
        """ Use the supplied test fixture """
        expected = 4
        actual = advent_18a('fixtures/aoc_18a_test.txt')
        self.assertEqual(expected, actual)

    def test_18b(self):
        """ Use the supplied test fixture """
        expected = 3
        actual = advent_18b('fixtures/aoc_18b_test.txt')
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
