# c.i:
for i in range (1, 10):
    for j in range (1, 10):
        print ("{0:<3}".format(i * j), end="")
    print()

# c.ii:
n = int(input("Enter a number: "))
for i in range (1, n + 1):
    for j in range (1, n + 1):
        print("{0:<3}".format(i*j), end="")
    print()
