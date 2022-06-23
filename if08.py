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

    string = ""

    if a > 9:
        if a % 2 == 1:
            string += "two-digit odd number"
        else:
            string += "two-digit even number"

    elif a > 99:
        if a % 2 == 1:
            string += "three-digit odd number"
        else:
            string += "three-digit even number"

    return string

print(main(57))