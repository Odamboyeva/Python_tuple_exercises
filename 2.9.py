my_tuple = ("hello", 5, "weather", "cat", 45, 78 )
numbers_tuple = tuple(value for value in my_tuple if isinstance(value, (int, float)))
print(numbers_tuple)
