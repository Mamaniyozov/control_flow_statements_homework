def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    if a>0 and b>0 and c>0:
        return "musbat sonlar 3ta"
    if a<0 and b>0 and c<0:
        return "musbat sonlar 1ta"
    if a>0 and b>0 and c<0:
        return "musbat sonlar 2 ta"
    if a<0 and b<0 and c>0:
        return "musbat sonlar 1ta"
    if a<0 and b>0 and c<0:
        return "musbat sonlar 2 ta"
    if a<0 and b<0 and c>0:
        return "musbat sonlar 1ta"
    if a<0 and b<0 and c<0:
        return "musbat son yuq"
    
print(main(-3,-1,-7)) 