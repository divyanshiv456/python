info = [
    ("khushi", "bio"),
    ("divyashi", "maths"),
    ("aarya", "commerce"),
    ("bagdh billa", "commere"),
    ("bhadu", "guu"),
    ("bhangi aulaad", "maths"),
    ("bhangi aulaad", "science"),
    ("khushi", "science")
]

# list all unique courses
unique_courses = set()
for tup in info:
    unique_courses.add(tup[1])  #course

print(unique_courses)

# list student enrolled in bio

for name, course in info:
    if(course == "bio"):
        print(name)

# create dictionary (student, set of course)

dict = {}
for name, course in info:
    if dict.get(name) == None:
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)    

print(dict)        