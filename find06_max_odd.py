def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i=0
    k=[]
    while i<len(data):
        if data[i]%2==1:
            k.append(data[i])
        i+=1
    return max(k)
print(find_max_odd([1, 8, 3, 8, 5]))
print(find_max_odd([11, 7, 5, 4, 9]))