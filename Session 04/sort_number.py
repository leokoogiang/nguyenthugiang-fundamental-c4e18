# Nhập vào dãy số [10, 2, -5,4]
# [-5, 2, 4, 10]
# Lập 1 mảng rỗng, hàm min và xóa nó đẩy vào mảng rỗng, lặp đi lặp lại đến khi len rỗng

# Nhập mảng vào
# A = [10, 2, -5,4]
# B = []

# for i in range(len(A)):

#     minNum = min(A)
#     B.append(minNum)
#     A.remove(minNum)

# print(B)


numbers = [10,-13,-5,4,0,9,2018]
sorted_list = []

while True: 
    min_numb = min(numbers)

    sorted_list.append(min_numb)

    numbers.remove(min_numb)

    if len(numbers) == 0:
        break

print(*sorted_list)
# print(min_number)
