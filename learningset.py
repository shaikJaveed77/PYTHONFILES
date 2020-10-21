#declaring the set
# tourism={"ladak" ,"scotland" ,"munnar"}
# print(tourism)
#
# tourism.add("lalbagh")
# print(tourism)

# for x in tourism:
#     print(x)
# del(tourism["lalbagh"])
# print(tourism)

# tourism.remove("lalbagh")
# print(tourism)
# tourism.add("cubbon park")
# print(tourism)
# tourism.add("bangalore fort", "wonderla")
# print(tourism)

# tourism.update(["bangalore fort" ,"wonderla"])
# print(tourism)
#
# tourism.add("ladak")
# print(tourism)

# tourism3=tourism.copy()
# tourism3["ladak"]="coorge"
# print(tourism3)

#set operations
#union operation
# tourism={"ladak" ,"scotland" ,"munnar"}
# # tourism2={"lalbagh" ,"cubban park"}
# # tourism2={"lalbagh" ,"cubban park" ,"ladak"}
# tourism3={"ladak","scotland","cubbon park"}
# unionset=tourism.union(tourism3)
# print(unionset)
#
# #intersection operation
# intersection2=tourism.intersection(tourism3)
# print(intersection2)
#
# # print(tourism3.issubset(tourism))
#
# print(tourism.issubset(tourism3))
#
# # checking difference
# print(tourism.difference(tourism3))
# print(tourism3.difference(tourism))

movies={"AA" ,"BB" ,"PP"}
print(movies)
movies.update(["RRR" ,"VIP"])
print(movies)
# movies.remove("PP")
movies.add("KGF")
print(movies)
# movies.clear()
# print(movies)
# another method for remove element is discard
# discard: this method is used to remove element
# it will not throw any error if the element is not in the set
movies.discard("PP")
print(movies)

movies.pop()
print(movies)



