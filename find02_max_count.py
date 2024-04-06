def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    return data.count(max(data))
print(find_max_count([1, 8, 3, 8, 5]))
print(find_max_count([13, 8, 3, 4, 9]))