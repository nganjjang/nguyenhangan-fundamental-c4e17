from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
n = 3 #number of angle
for i in range(5):
    color(colors[i])
    for j in range(i+n):
        forward(100)
        left(360/(i+n))
mainloop()
