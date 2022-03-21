import random



firstNames = ["Alicja", "Filip", "Ewa", "Krzys"]

name1, name2, name3, name4 = firstNames
u1_w = ran = random.randrange(0, 99)
print("""
Kto jest najgrubszy w rodzinie?
Jeśli chczesz sie tego dowiedzieć
patrz poniżej!
""")
"""
print(name1 + " waży : " + str(ran) + "kg.")
u2_w = ran = random.randrange(0, 99)
print(name2 + " waży : " + str(ran) + "kg.")
u3_w = ran = random.randrange(0, 99)
print(name3 + " waży : " + str(ran) + "kg.")
"""
u4_w = ran = random.randrange(0, 99)
#print(name4 + " waży : " + str(ran) + "kg.")

txt = "{}" + " waży : {} " + "kg."
print(txt.format(name4, u4_w))

"""
if u4_w >= 90:
    print("You are too heavy!")
else:
    print("You are ok.")

"""

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))