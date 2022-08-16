def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp < 0:
        temp = 'Freezing'
    elif temp > 0 and temp < 11:
        temp='Very Cold'
    elif temp > 10 and temp <21:
        temp='Cold'
    elif temp > 20 and temp <31:
        temp='Normal'
    elif temp > 30 and temp < 41:
        temp='Hot'
    elif temp > 40:
        temp='Very Hot'
    return temp
x=main(-105)
print(x)
