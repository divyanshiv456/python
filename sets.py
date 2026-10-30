# sets - collection of unique elements
s = {1, 2, 2, 2, 3}
print(s)
print(type(s))

#add
s.add(5)
print(s)

#empty set
empt_set = set()
print(type(empt_set))

#remove
s.remove(2)
print(s)

#pop - remove random value from the set
s.pop()
print(s)

#s.union(set2)
s1 = {1, 3, 4, 5, 7, 2}
s2 = {4, 7, 8, 12, 13}

print(s1.union(s2))

#s.intersection(set2)

print(s1.intersection(s2))