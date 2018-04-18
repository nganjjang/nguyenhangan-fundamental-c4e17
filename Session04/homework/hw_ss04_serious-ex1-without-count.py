#count without using count function:
list = [1, 6, 8, 1, 2, 1, 5, 6]
number = int(input("Enter a number?"))
count = 0
for n in list:
    if n == number:
        count += 1
print("{0} appears {1} times in my list".format(number, count))
