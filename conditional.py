age = int(input("enter your age: "))

if age < 13:
    print("your a child")
elif age >= 13 and age < 18:
    print("your a teenager")    
else:
    print("your an adult")    

color = input("enter color: ")

if color == "red":
    print("stop")
elif color == "yellow":
    print("look")
elif color == "green":
    print("go")  
else:
    print("wrong color for traffic light")          