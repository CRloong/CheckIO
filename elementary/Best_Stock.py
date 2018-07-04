'''
You are given the current stock prices. You have to find out which stocks cost more.

Input: The dictionary where the market identifier code is a key and the value is a stock price.

Output: A string and the market identifier code.

Example:

        best_stock({
            'CAC': 10.0,
            'ATX': 390.2,
            'WIG': 1.2
        }) == 'ATX'
        best_stock({
            'CAC': 91.1,
            'ATX': 1.01,
            'TASI': 120.9
        }) == 'TASI'


Preconditions: All the prices are unique.
'''


def best_stock(data):
    # your code here
    s = sorted(data.items(), key=lambda item: item[1], reverse=True)
    return s[0][0]


def best_stock_clear(data):
    return max(data, key=data.get)


def best_stock_speedy(data):
    return max(data.keys(), key=(lambda k: data[k]))


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")