balance=0
def main():
    while True:
        print("Welcome to the bank")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            deposit(int(input("Enter the amount to deposit: ")))
        elif choice == "3":
            withdraw(balance)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

print("Thank you and have a nice day!")





def show_balance(balance):
    print("Balance is: ", balance)




def deposit(n):
    global balance
    balance+=int(n)
    print("Deposit is: ", balance)
    return balance


def withdraw(n):
    global balance
    n=int(input("Enter the amount to withdraw: "))
    balance-=int(n)
    if n>balance:
        print("Insufficient amount to withdraw")
    elif n<0:
        print("Insufficient amount to withdraw")
    else:
        return n
    print("Withdraw is: ", balance)
    return balance


if __name__ == "__main__":
    main()