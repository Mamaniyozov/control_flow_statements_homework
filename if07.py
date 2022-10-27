from cgi import print_arguments


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
    if a%2==0:
        return "a juft son"
    if a%2==1:
        return "a toq son"
    if a>0:
        return "a musbat son"
    if a<0:
        return 'a manfiy son'
    if a==0:
        return "a nol"
print(main(0))