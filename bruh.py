
count_occurrences = ['B', 'A', 'B', 'C', 'A']


def count_occurrences(alist):
    count = {}
    for item in alist:
        if item in count:
            count[item] = alist[item]
        else:
            count[item] = 0
    return count