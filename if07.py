def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    message = ""

    if abs(a)%2 == 1 and a > 0:
        message += "positive odd number"
    
    elif abs(a)%2 == 0 and a > 0:
        message += "positive even number"

    elif abs(a)%2 == 1 and a < 0:
        message += "negative odd number"
    
    elif abs(a)%2 == 0 and a < 0:
        message += "negative even number"

    else:
        message += "the number is zero"


    return message

print(main(9))