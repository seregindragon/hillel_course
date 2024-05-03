import collections
b = dict.fromkeys([1,"a", 2, "b"])
print(b)

#get return value
print(b.keys()) # get keys
print(b.values()) # values
print(b.pop("name")) # return value and delete key and value
print(b.pop("name", "test")) # return value and delete key and value
b.popitem(last=false)
print(d)