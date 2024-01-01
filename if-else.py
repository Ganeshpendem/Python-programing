height=int (input("Given Height"))
if height>=5:
    print("Ok your allowed to ride")
    age=int(input("Given age"))
    if age<=12:
        print("Pay 150 per person")
    elif age<=18:
        print("250 per person")
    else:
        print("500 per person")
else:
    print("No Your not allowed to ride")
print("Thank you bye")