#d.i:
for i in range (10):
    for j in range (10):
        if (i + j) % 2 == 0:
            print("{0:<3}".format(1), end="")
        else:
            print("{0:<3}".format(0), end="")
    print()

#d.ii:
n = int(input("Enter a number: "))
for i in range (n):
    for j in range (n):
        if (i + j) % 2 == 0:
            print("{0:<3}".format(1), end="")
        else:
            print("{0:<3}".format(0), end="")
    print()
