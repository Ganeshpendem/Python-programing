order=input("your Order please: ")
bill=0
if order=="pizza":
    print("Which size of Pizza you need??")
    pizza_size=input("please enter size of pizza you need S/M/L: ")
    if pizza_size=="S":
        bill=100
        print(f"pizza price is {bill}")
        pepperoni=input("do you want Pepperoni Y/N: ")
        if pepperoni=="Y" or pepperoni=="y":
            bill+=30
            print(f"Extra 30 for pepperoni, and the total bill is {bill}")
    elif pizza_size=="M":
            bill=200
            print(f"pizza prize is {bill}")
            pepperoni=input("do you want Pepperoni Y/N: ")
            if pepperoni=="y":
                bill=bill+50
                print(f"Extra 50 for pepperoni, and the total bill is {bill}")
    else:
        bill=300
        print(f"pizza price is {bill}")
    extra_cheese=input("Do you want Extra Cheese on pizza? Y/N: ")
    if extra_cheese=="y":
        bill=bill+20
        print(f"the total bill is {bill}, enjoy your food have a great day")
else:
    print("Sorry we do not anything except Pizza")
print("thank you visit us again")



