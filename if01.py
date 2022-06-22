def main(a):
    """
    If the number is positive, increase it to 1, else leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    son = a
    if a > 0:
        son += 1

    else:
        son += 0

    return son

print(main(7))
