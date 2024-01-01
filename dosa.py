order = input("Hello order please: Dosa, Ildi,Pesara_dosa, punugulu: ")
bill = 0
count = int(input("How many you need: "))


if order == "Dosa":
    bill = 15
    print(f"{count},  Dosa please")


elif order == "Idli":
    bill = 10
    print(f"{count}, plate Idli please")

elif order == "Pesara_dosa":
    bill = 18
    print(f"{count},  Pesarattu please")

elif order == "punugulu":
    bill = 10
    print(f"{count}, plate Punugulu please")

else:
    print("Sorry we dont have anything except these: Dosa, Ildi,Pesara_dosa, punugulu")

bill = bill * (count)

print(f"Your total bill is: {bill}")

print("visit again thank you ")