# String - they are immutable (cannot be changed)

#len fun

word = "python"
print(len(word))

# concatination
word1 = "i like "
word2 = "python"

print(word1 + word2)

#indexing
print(word[2])

for i in word:
    print(i)

#slicing
# word[st ind : end ind(not included)]   

print(word[2:4])

# formating => dynamic strings (var & val)

a = 5
b = 6
sum = a + b
#normal formating
print("sum is {} and {} is {}".format(a, b, sum))
print("language is {}".format("python"))

#index base formating
print("sum is {1} and {0} is {2}".format(a, b, sum))

# value base formating
print("value of {a} and {b} ".format(a = 5, b = 10))

# F-string => literal string interpolation
x = 3
y = 4

print(f"avg of {x} and {y} is {(x + y)/2}")