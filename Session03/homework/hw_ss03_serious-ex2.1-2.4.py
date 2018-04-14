#2.1. Print flock size:
my_flock = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Ngan and these are my sheep sizes ")
print(my_flock)

#2.2. Choose the biggest sheep:
biggest_size = max(my_flock)
print("Now my biggest sheep has size", biggest_size, "let's shear it")

#2.3. Return biggest size to default value:
#print(my_flock.index(biggest_size))
my_flock[my_flock.index(biggest_size)] = 8
print("After shearing, here is my flock")
print(my_flock)

#2.4. In the following month, sheep sizes increase by 50:
print("One month has passed, now here is my flock")
for i in range (len(my_flock)):
    my_flock[i] = my_flock[i] + 50
print(my_flock)
#cach khac:
# for (i, val) in enumerate(my_flock):
#     my_flock[i] = val + 50
# print(my_flock)
