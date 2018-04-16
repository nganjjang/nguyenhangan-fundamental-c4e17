clothes = ["T-shirt", "Sweater"]
action = ["R", "C", "U", "D"]
input_shop = input("Welcome to our shop, what do you want (C, R, U, D)?")

if input_shop == "R":
    print("Our items: ", end="")
    print(*clothes, sep=", ")
    input_shop = input("Welcome to our shop, what do you want (C, R, U, D)?")
    if input_shop == "C":
        new_item = input("Enter new item: ")
        clothes.append(new_item)
        print("Our items: ", end="")
        print(*clothes, sep=", ")
        input_shop = input("Welcome to our shop, what do you want (C, R, U, D)?")

        if input_shop == "U":
            update_position = int(input("Update position? "))
            clothes[update_position-1] = input("New items? ")
            print("Our items: ", end="")
            print(*clothes, sep=", ")
            input_shop = input("Welcome to our shop, what do you want (C, R, U, D)?")

            if input_shop == "D":
                delete_position = int(input("Delete position? "))
                clothes.pop(delete_position-1)    #cach khac: del clothes[delete_position-1]
                print("Our items: ", end="")
                print(*clothes, sep=", ")

else:
    print("wrong input")
