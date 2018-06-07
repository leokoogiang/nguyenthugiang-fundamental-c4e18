# Ask users to enter a number n then calculate factorial of n (1*2...*n)

n = int(input('Enter the number '))

tich = 1

for i in range(1,n+1):
    tich *= i # Nhan va gan
print(tich)