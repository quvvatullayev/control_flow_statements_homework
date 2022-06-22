def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2. If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """

    
    son = a
    if a > 0:
        son += 1

    elif a < 0:
        son -= 2

    else:
        son += 10

    return son

print(main(0))