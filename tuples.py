#tuple - immutable sequence of values
tup = (1, 2, 3, 4, 5, "abc", 3.14)
print(tup)
print(type(tup))
print(len(tup))

print(tup[2])

tupp = (5)
print(type(tupp))

tuppp = ("abc",)
print(type(tuppp))

#silicing 
print(tup[2:])

#loop
sum = 0 
for i in tup:
    print(i)  

# tuple methods

# index(val) - return 1st occurence
tup1 = (1, 2, 3, 2, 3, 3, 4, 4)
print(tup1.index(4))


# count(val) - return total occurence

print(tup1.count(4))     