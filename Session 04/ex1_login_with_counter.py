# username = input("please enter your username: ")

# for i in range(3):
#     if username == "c4e":
#         password = input("please enter your password: ")
#         if password == "codethechange":
#             print("Welcome, c4e")
#         else:
#             print("password is incorrect")
        
#     else: 
#         print("you are not superuser")



print("Hi there this is a superuser gateway")
count = 0 # Khai báo biến count và gán cho nó giá trị 0

while True: 
    username = input("username: ")
    if username =="c4e":
        password = input("password: ")
        if password == "codethechange":
            print("Welcome!")
            break # Gặp break là không chạy đống lệnh ở phía dưới
        else:
            print("Password incorrect")
    else:
        print("You are not a superuser")


    count += 1
    if count == 3:
        print("You failed to login 3 times, go away")
        break
    





    


