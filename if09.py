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
    #12 and 21 false
    #75 and 57 true
    #11 and 11 true
    y = a%10 #7
    z = a//10 #5
    w = y * 10 +z
    if a >= w:
        a = 'True'
    else: 
        a='False'
    return a
x=main(11)
print(x)