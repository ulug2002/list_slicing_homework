def main(numbers):
    """
    A list called numbers is given. Return the items in the even index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    numbers = [1,2,3,4,5]
    return numbers[0::2]
print(main(numbers = 1))