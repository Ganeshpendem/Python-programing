#a=int(input("Enter number from (-1 to quit:  "))
#while a <=35:
#    print("your fail")
#    a = int(input("Enter number from (-1 to quit:  "))
#else:
#         print("Your Pass")

total=0
numbers=int(input("Enter the numbers from1 to quit : \n"))
while numbers >=0:
    total+=numbers
    numbers = int(input("Enter the numbers from1 to quit : \n"))
print(f"total is {total}")
