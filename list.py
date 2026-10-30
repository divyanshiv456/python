#list are mutable sequence of values
marks = [99, 98, 78, 65, 79]

print(marks)
print(len(marks))
print(marks[0])

marks[2] = 80
print(marks)

print(type(marks))

print(marks[0:2]) # slicing

#list specific methods

#append - add an element at the end
num = [1, 3]
num.append(4)
print(num)

#insert - insert element at ind
num.insert(1, 2)
num.insert(2, 10)
print(num)

#reverse - reverse order
num.reverse()
print(num)

#sort - arrange in increasing order
num.sort(reverse = True)
print(num)

#loop on list
t = [12, 3, 9, 5, 1, 10]

ind = 0
for i in t:
    if i == 4:
        print(ind)
        break
    ind += 1
else:
    print("not found")


