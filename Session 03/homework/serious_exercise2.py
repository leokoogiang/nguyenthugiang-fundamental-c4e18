sizes = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Hiep, there are my ships size')
print(sizes)
print('------------------------------------------------')

maxValue = max(sizes)
print('Now my biggest sheep has size', maxValue,) 
print('let us shear it')

sizes[sizes.index(maxValue)] = 8

print('After shearing, here is my flock')
print(sizes)
