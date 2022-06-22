def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else decreased by 2.
    """

    son = a
    if a > 0:
        son += 1

    else:
        son -= 2

    return son

print(main(-5))