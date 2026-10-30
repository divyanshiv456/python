def hello(): #fnx defination
    print("hello")

hello()    #fnx calling

def sum(a , b = 1):
    sum = a + b
    print(sum)

sum(12, 24)    

# avg of 3 nummbers

def avg(a, b, c):
    avg = (a + b + c)/3
    return avg

print(avg(2, 3, 4))

sum(5)

# factorial function


def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact    

print(cal_fact(5))