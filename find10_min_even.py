def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    i=0
    k=[]
    while i<len(data):
        if data[i]%2==0:
            k.append(data[i])
        i+=1
    return min(k)
print(find_min_even([1, 8, 2, 8, 5]))
print(find_min_even([7, 8, 4, 3, 5]))


