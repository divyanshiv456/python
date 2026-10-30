# dictionary - key:value pairs
# they are mutable and unordered

info = {
    "name": "khushi bhangi",
    "age": 16,
    "subject": ["kemistriii", "biologee"]
}

print(info)
print(type(info))

print(info["name"])

info["name"] = "khikhikhi"
print(info["name"])

#keys - return all the keys
#values - return all the values
print(info.keys())

# we can type caste dic into list
dict_keys = list(info.keys())
dict_vals = list(info.values())

print(dict_vals)
print(dict_keys)


print(type(dict_keys))

#items - return al the key values pair
print(info.items())

# get - signnifcance => it does not give error like keys

# print(info.keys("cgpa"))  error

print(info.get("cgpa"))
print("end of code")

#update - add new item in dictionary
info.update({
    "city":"ujjain"
})

print(info)