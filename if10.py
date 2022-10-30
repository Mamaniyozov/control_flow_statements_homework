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
    m=temp
    if m>0 and m<11:
        return 'very cold'
    elif m>10 and m<21:
        return 'cold'
    elif m>20 and m<31:
        return 'Normal'
    elif m>30 and m<41:
        return 'hot'
    else:
        return 'very hot'
print(main(45))