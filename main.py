

def is_leximin_better(x: list, y: list) -> bool:
    """
    >>> a = [9,10,90,43,23,32,12,17]
    >>> b = [7,23,12,13,17,15,78,77]
    >>> is_leximin_better(a, b)
    True

    >>> a = [9,10,90,43,23,32,12,17]
    >>> b = [17,23,12,13,17,15,78,77]
    >>> is_leximin_better(a, b)
    False

    >>> a = [10, 20, 15, 30]
    >>> b = [9, 12, 21, 15]
    >>> is_leximin_better(a, b)
    True

    >>> a = [16,22,12,13,17,15,78,77] # -> 12,13,15,16,17,~22~,77,78
    >>> b = [16,23,12,13,17,15,78,77] # -> 12,13,15,16,17,~23~,77,78
    >>> is_leximin_better(a, b)
    False

    >>> a = [16,23,12,13,17,15,78,77] # -> 12,13,15,16,17,~23~,77,78
    >>> b = [16,22,12,13,17,15,78,77] # -> 12,13,15,16,17,~22~,77,78
    >>> is_leximin_better(a, b)
    True

    >>> a = [16,22,12,13,17,15,78,77]
    >>> b = []
    >>> is_leximin_better(a, b)
    Traceback (most recent call last):
       ...
    AssertionError

    >>> a = [5,19,11,54,9,21,7,4,11,10] # ->  4,5,7,9,10,11,11,19,856,54
    >>> b = [11,9,21,7,531,4,5,19,11,10]  # -> 4,5,7,9,10,11,11,19,21,531
    >>> is_leximin_better(a, b)
    False

    >>> a = [5,44,11,54,9,856,7]
    >>> b = [5,44,11,54,9,856,7]
    >>> is_leximin_better(a, b)
    False

    """
    assert len(x) == len(y)
    x.sort()
    y.sort()
    i, j = 0,0
    while(i < len(x) and j < len(y)):
        if x[i] > y[j]:
            return True
        elif x[i] < y[i]:
            return False
        else:
            i, j = i + 1, j + 1
    return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import  doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
    # a = [5,44,11,54,9,856,7]
    #
    # b = [11,9,12,7,31,4,5,6,7,10]
    # a = [5, 44, 11, 54, 9, 856, 7]
    # b = [5, 44, 11, 54, 9, 856, 7]
    #
    # print(is_leximin_better(a, b))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
