#creating the dictionary
# {
#  'name' : 'j',
#  'batch' : 2020
# }

dev1={
    'name' : 'bhaskar',
    'qualification' : 'B.E',
    'batch' : 2020,
    'age' : 24
}
# reading the dictionary
# print(dev1.get('name'))
# print(dev1['qualification'])
# print(dev1['batch'])
# print(dev1['age'])

# updating the values

# print("updating bhaskar's age")
# dev1["age"]=25
# print(dev1["age"])

#deleting dict
# del dev1
del(dev1['age'])
# print(dev1.get('name'))
# print(dev1['qualification'])
# print(dev1['batch'])
# print(dev1['age'])

#another method of deleting

dev1.pop("batch")
print(dev1)

dev1.popitem()
#adding of new key to dictionary
dev1["city"] = "bangalore"
print(dev1)

#check whether the key exists
print("name" in dev1)

movie= {"hero": "aallu arjun", "heroine": "pooja", "title": "pushpa", "date": "coming soon"}
#adding one key

print(movie)

#deleting one key

del(movie["date"])
print(movie)

#updating the key value

movie["title"] = "AA"
print(movie)










