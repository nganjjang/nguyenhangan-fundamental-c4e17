my_flock = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Ngan and here is my flock ")
print(my_flock)
print()

for i in range(3):
    print("MONTH", i+1, ":")
    print("One month has passed, now here is my flock")
    for j in range (len(my_flock)):
        my_flock[j] = my_flock[j] + 50
    print(my_flock)
    biggest_size = max(my_flock)
    print("Now my biggest sheep has size", biggest_size, "let's shear it")
    my_flock[my_flock.index(biggest_size)] = 8
    print("After shearing, here is my flock")
    print(my_flock)
    print()
