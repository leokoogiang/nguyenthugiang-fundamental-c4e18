from turtle import*
color('blue')
speed(-1)
num_shape = int(input('Please enter the number of shape you want: '))
length = 10

for j in range(num_shape):
    for i in range(4):
        forward(length)
        left(90)
    left(360/num_shape)
    length +=5

mainloop()
