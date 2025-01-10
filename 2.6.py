mytuple = ("apple", "banana", "cherry")
mylist = list(mytuple)
if "banana" in mylist:
    index = mylist.index("banana")
    mylist[index] = "pear"

mytuple = tuple(mylist)
print(mytuple)