def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    
    p = 0
    n = 0

    if a < 0:
        p += 1
    
        if b < 0:
            p += 1

        if c < 0:
            p += 1

    if a > 0:
        n += 1
    
        if b > 0:
            n += 1

        if c > 0:
            n += 1

    if p > n:
        return "negative numbers"

    return "positive numbers"


print(main(-8,9,8))