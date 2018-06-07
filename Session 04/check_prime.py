# Kiểm tra số người dùng nhập vào có phải là prime hay không
# num = int(input("Please enter a number: "))


# if num ==2:
#     print("2 is a prime number")
# else: 
#     for i in range(2,num):
#         if (num % i) == 0:
#             print("The number you enter is not a prime number")
#             break
           
#         else:
#             print(num, "is a prime number")

# Tầng 1 khai báo, tầng 2 process, tầng 3 khai báo
# Input
num = int(input("Please enter a number: "))
is_prime = True

# Process
for i in range(2,num):
    if (num%i==0):
        is_prime = False
        break

# True == True => True
# False == True => False
# output
if is_prime: #== True
    print("{0} is a prime number".format(num))
else:
    print("{0} is not a prime number".format(num))