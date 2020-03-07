tupla1 = (0,"elemento 1", 2.1, "elemento 1")
tuplaVacia = ()
tuplaUnica = (100,)

print(tupla1[2])
print(tupla1.count(0))
print(tupla1.index("elemento 1",2))


set1 = set([1,2,3,4,5,6])
set2 = set((4,5,6,7,8))

set2.add(6)
print(set2)

print(set1.difference(set2))
print(set1.intersection(set2))
print(set1.issuperset(set([2,3,4])))
print(set1.discard(1), set1)

