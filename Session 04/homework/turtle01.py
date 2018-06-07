from turtle import*
color('blue')
speed(-1)

num_sq = int(input('Please enter the number of square that you want: '))

for j in range(num_sq):
    left(360/num_sq)

    for i in range(4):
        forward(100)
        left(90)
    

mainloop()