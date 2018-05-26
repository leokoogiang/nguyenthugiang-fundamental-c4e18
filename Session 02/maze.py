from turtle import * 
speed(-1)
shape('turtle')

length = 5 # set san quang duong cua con turtle

for i in range(80): # tac dong vao start stop step cua vong for 
    forward(i) # i luon tang sau moi vong lap, step cua vong for
    left(90)

    length += 5 #length = length + 5

mainloop()