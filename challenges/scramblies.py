from collections import Counter 
def scramble(s1, s2):
    s1_items = Counter(s1).items()
    s2_items = Counter(s2).items()

    d1 = {}
    d2 = {}
    for (key1, value1), (key2, value2) in zip(s1_items, s2_items):
        d1[key1] = value1
        d2[key2] = value2

    for l in d2:
        if not(l in d1 and d2[l] <= d1[l]):
            return False
    return True
