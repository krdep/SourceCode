
# Print list with list orders
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(str(i) + ". " + thislist[i])


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(str(i) + thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]