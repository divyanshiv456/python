# 1
# salary = int(input("enter your salary: "))

# if salary < 30000:
#     print("your final tax 5%")
# elif salary == 30000 or salary < 70000:   
#     print("your final tax 15%")
# else: 
#     print("your final tax 25%")

# #2
# a = int(input("enter a number: "))
# b = int(input("enter another number: "))

# def cal_prime(a, b):
#     for i in range(a, b+1): 
#         if i > 1:
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             else:
#                 print(i)   



# cal_prime(a, b)       

#3
# n = int(input("enter any number: "))

# def digi(n):
#        while n > 0:
#               digit = n % 10
#               print(digit)
#               n = n//10
              
        
# digi(n)          

#4

# num = int(input("enter a nmber: "))

# def digit_count(n):
#     count = 0
#     while n > 0:
#         digit = n % 10
#         count += 1
#         n = n//10

#     print(count)    

# digit_count(num)

#5

# num = int(input("enter any number: "))

# def digit_sum(n):
#     sum = 0
#     while n > 0:
#         digit = n % 10
#         sum += digit
#         n = n//10
#     print(sum)    

# digit_sum(num)

#6

# for i in range(1, 100):
#     if(i % 3 == 0 and i % 5 == 0):
#         print(i)

#7

# while True:
#     num = input("enter a number or quit: ")

#     if num == "quite":
#         print("program stoped! ")
#         break
#     num = int(num)
#     if num > 0:
#         print("positive")
#     elif num < 0: 
#         print("negetive")   
#     else:
#         print("Zero")           

#8

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# op = input("enter the operator: ")

# def calculator(a, b, op):
#     if op == "+":
#         print(a+b)
#     elif op == "-":
#         print(a-b)
#     elif op == "*":
#         print(a*b)
#     elif op == "/":
#         print(a/b)
#     else:
#         print("undefined operator")  

# calculator(a, b, op)                              

#9

# n = int(input("enter a number: "))

# def is_prime(n):
#        if n <= 1:
#               return False

#        for i in range(2, n):
#               if n % i == 0:
#                      return False
              
#        return True      

# print(is_prime(n))

#10



while True:
       target = 4
       n = int(input("enter any number: "))

       if n == target:
              print("correct")
              break
       elif n > target:
              print("number is too high")   
       else:
              print("number is too low")
                      