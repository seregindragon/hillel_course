s = "hello" # bit-string

b = s.encode("utf-8")

print(type(b))
print(b)


s = b.decode("utf-8")


print(type(s))
print(s)