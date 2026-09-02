def union(set1, set2):
    return set1 | set2


def intersection(set1, set2):
    return set1 & set2


def difference(set1, set2):
    return set1 - set2


def symmetric_difference(set1, set2):
    return set1 ^ set2


set1 = set(map(int, input("Enter the first set: ").split()))
set2 = set(map(int, input("Enter the second set: ").split()))

print("Union:", union(set1, set2))
print("Intersection:", intersection(set1, set2))
print("Difference (Set 1 - Set 2):", difference(set1, set2))
print("Difference (Set 2 - Set 1):", difference(set2, set1))
print("Symmetric Difference:", symmetric_difference(set1, set2))
