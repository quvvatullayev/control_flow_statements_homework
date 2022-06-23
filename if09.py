def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """

    if 9 < a < 10:
        a1 = a % 10
        a = a // 10

        a2 = a % 10
        a = a // 10

        son = a1 * 10 + a2
        javob = ""

        if son  <= a:
            javob += "True"
        
        else:
            javob += "Fals"

    return javob

print(main(45))