#assignment
name = input("enter your name: ")
age = input("enter your age: ")

print("hello " + name + ", you are " + age + " year old!" )

a = int(input("enter a number: "))
b = int(input("enter another number: "))

print(a+b)
print(a-b)
print(a*b)
print(a/b)

x = int(input("enter an integer: "))
y = int(input("enter an another integer: "))
z = float(input("enter a float: "))
float(x)
float(y)

avg = (x + y + z) / 3
print(avg)
print(type(avg))

num = input("enter a number: ")
print(type(num))

print(type(int(num)))
print(type(float(num)))
print(type(str(num)))


x = 10 + 3 * 2 ** 2
print(x)

# #swap
v1 = int(input("enter v1 number: "))
v2 = int(input("enter v2 number: "))

v = v1
v1 = v2
v2 = v
print("value of v1 " , v1)
print("value of v2 " , v2)

#temperature
cel_temp = input("enter the temp in celsius: ")
farhenheit_temp = (float(cel_temp) * (9/5)) + 32
print(farhenheit_temp)

# #area
r = float(input("enter the radius of circle: "))
pi = 3.14
area = pi * r ** 2
print("area of cirle is ", area)

#simple intrest
p = input("enter principle: ")
r = input("enter rate: ")
t = input("enter time: ")

SI = (float(p) * float(r) * float(t)) / 100

print("simple intrest : ", SI)

#parts 
num = float(input("enter any number: "))
i = int(num)
print(i)
fractional = num - float(i)
print(fractional)
