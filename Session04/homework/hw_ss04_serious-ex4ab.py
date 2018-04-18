#a.i:
for i in range (20):
    print(i, end=" ")
print()

#a.ii:
n = int(input("Enter a number: "))
for i in range(n):
    print(i, end= " ")
print()

#b.i:
for i in range (20):
    if i % 2 == 0:
        print(1, end=" ")
    else:
        print(0, end=" ")
print()

#b.ii:
n = int(input("Enter the total number of 1's and 0's: "))
for i in range (n):
    if i % 2 == 0:
        print(1, end=" ")
    else:
        print(0, end=" ")
print()
