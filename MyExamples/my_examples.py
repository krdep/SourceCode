# Using format
userName = "Krzys"
userWeight = random.randrange(0, 99)
txt = "{}" + " waży : {} " + "kg."
print(txt.format(userName, userWeight))

quantity = 3 
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


