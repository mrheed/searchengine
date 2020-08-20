"""
File: common_elements.py
------------------------
File to implement a function that is passed two lists and returns a new list
containing those elements that appear in both of the lists passed in.
"""


def common(list1, list2):
    """
    This function is passed two lists and returns a new list containing
    those elements that appear in both of the lists passed in.
    """
    ret = []
    for i, v in enumerate(list1):
        for j in list2:
            if v == j:
                if len(ret) == 0:
                    ret.append(v)
                    break
                if ret[len(ret)-1] != v:
                    ret.append(v)
                    break

    return ret

    
    """
    You implement this function.  Don't forget to remove the 'pass' statement above.
    """


def main():
    print(common(['a'], ['a']))                             # should print ['a']
    print(common(['a', 'b', 'c'], ['x', 'a', 'z', 'c']))    # should print ['a', 'c']
    print(common(['a', 'b', 'c'], ['x', 'y', 'z']))         # should print []
    print(common(['a', 'a', 'b'], ['a', 'a', 'x']))         # should print ['a']


if __name__ == '__main__':
    main()
