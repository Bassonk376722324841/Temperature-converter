def round_ans(val):
    '''
    Rounds temperatures to nearest degree
    :param val: Number to be rounded
    :return: Number rounded to nearest degree
    '''

    try:
        var_rounded = (val * 2 + 1) // 2
        return "{:.0f}".format(var_rounded)

    except ValueError:
        print("Given value to round isn't a valid number")


def to_celsius(to_convert):
    '''
    Converts from F to C
    :param to_convert: Temperature to convert into C
    :return: Converted temperature in C
    '''

    try:
        answer = (to_convert - 32) * 5 / 9
        return round_ans(answer)

    except ValueError:
        print("Given value to round isn't a valid number")


def to_fahrenheit(to_convert):
    '''
    Converts from C to F
    :param to_convert: Temperature to convert into F
    :return: Converted temperature in F
    '''

    try:
        answer = to_convert * 1.8 + 32
        return round_ans(answer)

    except ValueError:
        print("Given value to round isn't a valid number")


# Main routine (testing functions)
to_c_test = [0, 100, -459]
to_f_test = [0, 100, 40, -273]

for item in to_f_test:
    ans = to_fahrenheit(item)
    print(f"{item} C is {ans} F")

print()

for item in to_c_test:
    ans = to_celsius(item)
    print(f"{item} F is {ans} C")