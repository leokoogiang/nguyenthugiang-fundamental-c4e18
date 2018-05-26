from turtle import * 
speed(-1)
shape("turtle")
color("green")
fillcolor('green')
n=int(input("Number of side?"))

for i in range(n):
    forward(50)
    left(360/n)


#for i in range(1):



mainloop()