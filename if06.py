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
    son = ""
    numbers_sal = 0
    numbers_ijobiy = 0

    if a < 0:
        numbers_sal += 1
    
    if b < 0:
        numbers_sal += 1

    if c < 0:
        numbers_sal += 1

    if a > 0:
        numbers_ijobiy += 1
    
    if b > 0:
        numbers_ijobiy += 1

    if c > 0:
        numbers_ijobiy += 1

    if numbers_ijobiy > numbers_sal:
        son += "positive numbers"

    if numbers_ijobiy < numbers_sal:
        son += "negative numbers"

    return son

print(main(-8,9,8))