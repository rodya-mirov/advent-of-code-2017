""" Code supporting day 2 of advent; no tests because it's too simple """

def advent_2_a(spreadsheet):
    """ Determine the checksum of the given spreadsheet """
    total = 0

    for row in spreadsheet:
        less = row[0]
        more = row[0]
        for i in row[1:]:
            less = min(less, i)
            more = max(more, i)

        total += more - less

    return total

def advent_2_b(spreadsheet):
    """ Determine the checksum of the given spreadsheet """
    total = 0

    def find_pair(row):
        """
        Find the unique pair (a,b) in the row where a|b, and return b // a

        This assumes there really is a unique pair, and returns the first one found.
        Behavior not specified if there are multiple pairs. If there is no pair, raises
        an error.
        """
        for i in range(1, len(row)):
            a = row[i]
            for j in range(0, i):
                b = row[j]
                if a % b == 0:
                    return a // b
                elif b % a == 0:
                    return b // a

        print("Could not find pair in row:", row)
        raise "FML"

    for row in spreadsheet:
        total += find_pair(row)

    return total
