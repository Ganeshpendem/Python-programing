height=float(input("your height: "))
bill=0
if height>=3:
    print("Yes your allowed to ride")

    age=int(input("please enter your age"))
    if age<=12:
        bill=50
        print("Ticket price is  $50")
    elif age <= 18:
        bill=75
        print("Ticket price is  $75")
    else:
        bill=100
        print("Ticket price is  $100")
    want_photo=input("Do you want photo while riding")
    if want_photo=="Yes" or want_photo=="yes":
        print("Extra $10 for Photo")

        bill=bill+20
    print(f"your total bill is {bill}")
    print("Enjoy the ride")
else:
    print("Sorry you are not allowed to Ride")
    print("Better luck next time")
print("Bye Bye")


