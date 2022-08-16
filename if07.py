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
    if a==0:
        a ='the number is zero'
    elif a<0:
        if a%2:
            a = 'negative odd number'
        else:
            a = 'negative even number'
    elif a%2:
        a = 'positive odd number'
    else:
        a = 'positive even number'
    return a
x=main(10)
print(x)