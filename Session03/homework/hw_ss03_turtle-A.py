from turtle import *
n = 3 #number of angle
for i in range(4):
    for j in range(i+n):
        if (i+n) % 2 == 0:
            color("red")
        else:
            color("blue")
        forward(100)
        left(360/(i+n))
mainloop()
