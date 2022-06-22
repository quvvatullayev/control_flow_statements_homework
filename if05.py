def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    numbers = 0

    if a < 0:
        numbers += 1
    
    if b < 0:
        numbers += 1

    if c < 0:
        numbers += 1

    return numbers

print(main(-7,8,-9))