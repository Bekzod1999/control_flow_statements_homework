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
    if a > 99 or a < -99:
        if a % 2:
            a = 'three-digit odd number'
        else:
            a = 'three-digit even number'
    elif a < 99 and a > -100:
        if a%2:
            a = 'two-digit odd number'
        else:
            a = 'two-digit even number'
    return a
x = main(0)
print(x)