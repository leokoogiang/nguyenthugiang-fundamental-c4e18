# Ask a user to enter a number n, then print n 1's and 0's in total consecutively

n = int(input("Please enter the number "))

for i in range(n):
    if i%2==0:
        print('1', end='')
    else:
        print('0', end='')