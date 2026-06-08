# Exercise Banking program

def show_balance(balance):
    print("*********************")
    print(f"Your balance is: ${balance:.2f}")
    print("*********************")


def deposit():
    print("*********************")
    amount = float(input("Enter an amount to be deposited: $"))
    print("*********************")

    if amount < 0:
        print("*********************")
        print("That's not a valid amount")
        print("*********************")
        return 0
    else:
        return amount


def withdraw(balance):
    print("*********************")
    amount = float(input("Enter an amount to be withdrawn: $"))
    print("*********************")

    if amount < 0:
        print("*********************")
        print("Amount must be greater than 0")
        print("*********************")
        return 0
    elif amount > balance:
        print("*********************")
        print("Insufficient funds")
        print("*********************")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("  Banking Program  ")
        print("*********************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*********************")

        choice = input("Enter your choice (1-4): ")

        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
                print("DONE!")
            case "3":
                balance -= withdraw(balance)
                print("DONE!")
            case "4":
                is_running = False
            case _:
                print("*********************")
                print("that is not a valid choice")
                print("*********************")

    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")


if __name__ == '__main__':
    main()
