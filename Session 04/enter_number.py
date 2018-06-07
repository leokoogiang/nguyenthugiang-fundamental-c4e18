s = input('Enter your sequence of number, separated by space: ')

words = s.strip().split(" ") # Hàm strip bỏ dấu cách ở đầu và cuối

numbers = []

for item in words:
    numbers.append(int(item))

print(numbers)

# Kiểm tra xem list nhập vào đã sắp xếp chưa còn không săp xếp lại

# Số đằng trc và số đằng sau, nếu số sau lớn hơn số trc, dãy đã sắp xếp


in_sorted = True # Lưu trạng thái
for i in range(len(numbers)-1):
    if numbers[i]>numbers[i+1]:
        is_sorted = False
        break

if is_sorted: # Không cần thiết = True:
    print("Your sequence is sorted")
else: 
    print("Your sequence is not sorted")
    sorted_list=[]
    while True:
        min_numb = min(numbers)
        sorted_list.append(min_numb)
        numbers.remove(min_numb)
        if len(numbers) == 0:
            break
print("After sort:", *sorted_list)


# Nếu chưa sắp xếp hãy sắp xếp lại


    
# for i in range(len(words)):
#     if i<(i+1):
#         print(numbers)
#         break
#     else: 
#         while True: 
#             min_numb = min(numbers)

#             sorted_list.append(min_numb)

#             numbers.remove(min_numb)

#             if len(numbers) == 0:
#             break

#     print(*sorted_list) 
