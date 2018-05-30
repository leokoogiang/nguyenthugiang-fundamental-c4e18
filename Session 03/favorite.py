favs = [
    'death note',
    'netflix',
    'teaching'
]
print('Hi there, here is your favorite list')

print(*favs, sep=', ' )
print('****')
position = int(input('Position you want to update: '))
update_fav = input('Your replacing fav? ')
favs[position - 1] = update_fav
for index, item in enumerate(favs):
    print('{0}.{1}'.format(index+1, item))

# new_fav = input('Name one thing you like more')

favs.append('coding')
first_item = favs[1]
for i in range(5):
    print(first_item)

favs[1]='coding'
print(*favs, sep=', ' )

