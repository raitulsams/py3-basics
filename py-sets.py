set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set1.difference(set2)
set6 = set1.symmetric_difference(set2)  # reverse of intersection
set1.difference_update(set2)
print(set1)

# in-place method (it modifies the original set).
# non-in-place method (it returns a new set).
