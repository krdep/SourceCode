
"""
l1 = ["apple", "banana", "cherry"]

l2 = [l1[2], l1[0], l1[1]]

print(l1)

print(l2)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:])

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
"""
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(str(i) + ". " + thislist[i])