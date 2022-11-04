def main(list1,n):
    """
    A list of several elements is given. Return all items from end n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    if n>0:
        return list1[::0-n]
    return list1[::n]
print(main(('a','b','c','d','e','f'), 2 ))