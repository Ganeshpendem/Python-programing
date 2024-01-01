order = input("Hello Order Please: ")
bill = 0
if order == "tea":
    bill = 10
    print("What type of tea you need, masala, ginger, normal")
    order = input("type of tea masala, ginger, normal: ")

    if order == "masala":
        bill += 5
        print("one masala tea please")
    elif order == "ginger":
        bill += 3
        print("One ginger tea please")
    elif order == "Normal":
        bill = bill
        print("one normal tea please")
    else:
        print("We dont have other choice")
    count_tea = input("How many tea/coffee you need?: ")
    bill = bill * int(count_tea)

else:
    print("We dont have other options to order sorry")
print(f"your total bill is {bill}")

print("thanks for coming visit again ")