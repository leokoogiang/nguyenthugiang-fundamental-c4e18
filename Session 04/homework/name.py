name = input('Your full name: ')

name_1 = name.split()
length = len(name_1)

name_2 = []

name_3 = []

for i in range(0, length):
    name_2.append(name_1[i].lower())
    name_3.append(name_2[i].title())
    name = str.join(" ",name_3)

print("Updated: ",name)
