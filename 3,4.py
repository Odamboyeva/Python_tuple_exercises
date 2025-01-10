#(unpack) exercises
fruit = ("apple", "banana", "cherry", "orange", "grape")
tropical, *citrus = fruit

tropical = fruit[:2]
citrus = fruit[2:]

print(tropical)
print(citrus)