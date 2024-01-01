def deposit():
    while True:
        amount = input("what would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater then 0.")
        else:
            print("please enter a number.")
            return amount
def get_number_of_lines():

    def main():
        balance = deposit()

    main()