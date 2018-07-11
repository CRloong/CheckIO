"""
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.

Input: a list of strings.

Output: a string.
"""

from collections import Counter


def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    print(Counter(data).most_common(1)[0][0])
    return Counter(data).most_common(1)[0][0]


def most_frequent_speedy(data:list) -> str:
    return max(set(data), key=data.count)


def most_frequent_speedy2(data:list) -> str:
    # return max(data, key=lambda a: data.count(a))
    return max(data, key=data.count)


if __name__ == '__main__':
    l1 = ('a', 'a', 'a', 'b', 'b', 'c')
    l2 = ['a', 'a', 'bi', 'bi', 'bi']
    l3 = ['b', 'a', 'b', 'a', 'a', 'b']
    l3.sort()
    # print(most_frequent(l1))
    print(most_frequent_speedy2(l3))

