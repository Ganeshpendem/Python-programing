height=int(input("Given Height:"))

if height>=3:
    print("Ok you can ride")
    age=int(input("Given Age:"))
    if age<12:
        print("pay 250")
    else:
        print("pay 500")
else:
    print("Not allowed to ride")
print("Thank you Bye")