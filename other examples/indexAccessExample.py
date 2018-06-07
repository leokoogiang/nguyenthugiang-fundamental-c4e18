fruitList = ['apple', 'apricot', 'banana', 'coconut', 'lemon']
print(fruitList)

# Số phần từ
print('Element count', len(fruitList))

for i in range (0, len(fruitList) ) :
    print('Element at', i, '=', fruitList[i])

# Danh sách con chứa các phần tử index 1 đến 4
subList = fruitList[1:4]
print('Sub list [1:4]', subList)