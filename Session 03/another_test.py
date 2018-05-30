# Save food in a menu
# food1 = 'Salad Nga'
# food2 = 'Chocolate'
# food3 = 'So'
# food4 = 'Mi tom'
# food5 = 'Pho'

# list (array)
# Create
menu = [
    'Salad Nga',
    'Chocolate',
    'So',
    'Mi tom'
    
]

# seperator
# Read
# print(*menu, sep=', ')
# print(len(menu))

# Update one more item
menu.append('Banh muot')



# print((*menu), sep=', ')
# print(len(menu))
first_item = menu[1]
for i in range(len(menu)):
    print('{0}. {1}'.format(i+1, menu[i]))
    #print(i+1,'. ',menu[i],sep='')
    # duyet for theo index
print('******')
for index, item in enumerate(menu):
    print('{0}. {1}'. format(index+1, item))

print('****')
# for item in menu:
#     print(item)

# Get the number of 

# Tim vi tri index
menu[2] = 'Cua'

print(*menu, sep=', ')