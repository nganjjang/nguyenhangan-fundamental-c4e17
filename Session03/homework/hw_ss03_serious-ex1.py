#R exercise:
print("Welcome to our shop, what do you want (C, R, U, D)?")
clothes = ["T-shirt","Sweater"]
print("Our items: ", end="")
print(*clothes, sep=", ")

#C exercise:
new_item = input("Enter new item: ")
clothes.append(new_item)
print("Our items: ", end="")
print(*clothes, sep=", ")

#U exercise:
update_position = int(input("Update position? "))
clothes[update_position-1] = input("New items? ")
print("Our items: ", end="")
print(*clothes, sep=", ")

#D exercise:
delete_position = int(input("Delete position? "))
clothes.pop(delete_position-1)    #cach khac: del clothes[delete_position-1]
print("Our items: ", end="")
print(*clothes, sep=", ")
