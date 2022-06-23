from cgi import print_arguments


def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """

    s = ""

    if a > 9:
        if a % 2 == 1:
            s += "two-digit odd number"
        else:
            s += "two-digit even number"

    elif a > 99:
        if a % 2 == 1:
            s += "three-digit odd number"
        else:
            s += "three-digit even number"

    return s

print(main(57))