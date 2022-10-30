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
    a=323
    s=""
    if a<99 and a<1000:
        s+="three digit"
        if a%100%10%2==1:
            return '3xonali toq son'
    if a>9 and a<100:
        s+="two digit"
        if a%10%2==1:
            return '2 xonali toq son'
    
    if a%10%2==0:
        return '2xonali juft son '
    if a%100%10%2==0:
        return '3 xonali juft son'
