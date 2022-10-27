def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    if a<0 and b<0 and c<0:
        return "manfiy sonlar 3 ta"
    if a>0 and b<0 and c<0:
        return "manfiy sonlar 2ta"
    if a<0 and b>0 and c>0:
        return "manfiy sonlar 1ta"
    if a>0 and b>0 and c<0:
        return "manfiy sonlar 1 ta"
    if a>0 and b<0 and c>0:
        return "manfiy sonlar 1ta"
    if a>0 and b>0 and c>0:
        return "musbat sonlar "
    if a<0 and b>0 and c<0:
        return "manfiy sonlar 2ta"
print(main(-2,3,-2))