""" Code supporting the first day of advent. No tests because it's too simple! """

def advent_1_a(input_string):
    """ Determine the total of all digits which are equal to the subsequent digit """
    length = len(input_string)
    total = 0
    for i in range(0, length):
        if input_string[i] == input_string[(i+1) % length]:
            total += int(input_string[i])

    return total

def advent_1_b(input_string):
    """ Determine the total of all digits which are equal to the antipodal digit """
    length = len(input_string)
    total = 0
    for i in range(0, length):
        if input_string[i] == input_string[(i + (length//2)) % length]:
            total += int(input_string[i])

    return total
