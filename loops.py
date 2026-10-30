count = 1
while count <= 5:
    print("WOW")
    count += 1

# 6 table
count = 1
while count <= 10:
    print( 6 * count)
    count += 1

#odd num
# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i +=1

# for loop (sequencial loop)

string = "Div"
 # in => membership operator (to check presence)
for var in string:
    print(var)

if "v" in string:
    print("v exsits in loop")    

for k in range(5):
    print(k)    

# vowel count
count = 0
word = "artificial"

for ch in word:
    if(ch == "i" or ch == "o" 
       or ch == "a" or ch == "e" or ch == "u"):
        count += 1
    print(count)  

# range() => this function generate sequence  
# range(start, stop, step) 

# i = 0
# for i in range(i, 10, 2):
#     print(i)


# sum of n numbers
num = int(input("enter any number: "))

for t in range(1, num):
    print(t)