"""
Solutions to the "Advent of Code" toy problems
"""
import sys
import time

import days.advent01 as advent01
import days.advent02 as advent02
import days.advent03 as advent03
import days.advent04 as advent04
import days.advent05 as advent05
import days.advent06 as advent06
import days.advent07 as advent07
import days.advent08 as advent08
import days.advent09 as advent09

def do_puzzle(day, args):
    """ Do the puzzle specified by the user command line input """
    start_time = time.time()

    if day == "1a":
        print(advent01.advent_1_a(args[0]))
    elif day == "1b":
        print(advent01.advent_1_b(args[0]))
    elif day == "2a":
        with open("fixtures/aoc_2.txt") as input_file:
            rows = [[int(cell) for cell in line.split()] for line in input_file.readlines()]
            print(advent02.advent_2_a(rows))
    elif day == "2b":
        with open("fixtures/aoc_2.txt") as input_file:
            rows = [[int(cell) for cell in line.split()] for line in input_file.readlines()]
            print(advent02.advent_2_b(rows))
    elif day == "3a":
        num = 368078
        print(advent03.advent_3a(num))
    elif day == "3b":
        num = 368078
        print(advent03.advent_3b(num))
    elif day == "4a":
        print(advent04.advent_4a("fixtures/aoc_4.txt"))
    elif day == "4b":
        print(advent04.advent_4b("fixtures/aoc_4.txt"))
    elif day == "5a":
        print(advent05.advent_5a("fixtures/aoc_5.txt"))
    elif day == "5b":
        print(advent05.advent_5b("fixtures/aoc_5.txt"))
    elif day == "6a":
        print(advent06.advent_6a("2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"))
    elif day == "6b":
        print(advent06.advent_6b("2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"))
    elif day == "7a":
        print(advent07.advent_7a("fixtures/aoc_7.txt"))
    elif day == "7b":
        print(advent07.advent_7b("fixtures/aoc_7.txt"))
    elif day == "8a":
        print(advent08.advent_8a("fixtures/aoc_8.txt"))
    elif day == "8b":
        print(advent08.advent_8b("fixtures/aoc_8.txt"))
    elif day == "9a":
        print(advent09.advent_9a("fixtures/aoc_9.txt"))
    elif day == "9b":
        print(advent09.advent_9b("fixtures/aoc_9.txt"))
    else:
        print("Unrecognized day:", day)

    end_time = time.time()
    print("Took {:0.3f} seconds".format(end_time - start_time))

do_puzzle(sys.argv[1], sys.argv[2:])
