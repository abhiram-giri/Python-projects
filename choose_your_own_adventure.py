name = input("Enter your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are ona adirt road, it has come to and end and you can go left or right.Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles. ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles. ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You losw.")