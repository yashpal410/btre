set1 = {1,2,3,4,5,6,7,8}
set2 = {5,10,12,18,8}
set3 = {1,2,4}
print(set1)
set1.remove(2)
#print(set1)
#set1.remove(10)
print("After Removing 2",set1)
set1.add(2)
print("After adding 2",set1)
print("difference",set1.difference(set2))
print("difference",set2.difference(set1))
print("difference_update",set1.difference_update(set2), set1, set2)
print("difference_update",set2.difference_update(set1), set2, set1)
set1 = {1,2,3,4,5,6,7,8}
set2 = {1,5,10,12,18,8}
set3 = {1,2,4}
print("discard",set1.discard(3), set1)
print("discard",set1.discard(11), set1)
print("intersection",set2.intersection(set1),set1,set2)
print("intersection",set3.intersection(set2,set1), set1 ,set2 ,set3)
print("intersection_update",set2.intersection_update(set1), set1, set2)
print("intersection_update",set3.intersection_update(set2,set1),set1, set2, set3)
set1 = {1,2,3,4,5,6,7,8}
set2 = {1,5,10,12,18,8}
set3 = {1,2,4}
print("issubset",set3.issubset(set1))
print("issuperset",set1.issuperset(set3))
print("isdisjoint",set1.isdisjoint(set2))
print("pop",set1.pop())
print(set1)
set1 = {1,2,3,4,5,6,7,8}
set2 = {1,5,10,12,18,8}
set3 = {1,2,4}
print("symmetric_difference",set1.symmetric_difference(set2),set1, set2)
print("symmetric_difference_update",set1.symmetric_difference_update(set2), set1 ,set2)
print("union",set1.union(set2), set1, set2)
print("update",set1.update(set2),set1, set2)

