def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    list1 = ['a','d','g','k','o','y']
    n = 3
    return list1[n:][::-1]
print(main(list1=1,n=1))