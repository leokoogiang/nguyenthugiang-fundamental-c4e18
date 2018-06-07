# Nghĩ ra 1 số và để cho số đoán
# Tạo ra 2 biến low và high, và mid 
# mid có giá trị bằng (low+high)/2
# mid dịch chuyển
# input

print("Now think of a number from 0 to 100, then press Enter")
input()
print("""
All you have to do is to answer to guess
'c' if my number is 'C"orrect
's' if my guess is 'S'mall than your number
'l' if my guess is 'L'arger than you number

""")

low = 0
high = 100

while True: 

    mid = (low+high)//2

    ans = input("Is {0} your number ".format(mid)).upper()

    if ans == 'C':
        print('I knew it')
        break
        
    elif ans == 'S':
        low = mid
    elif ans == 'L':
        high = mid
    else:
        print('Ezzz')



