bank_balance = 0


def deposit(amount):
    global bank_balance
    bank_balance += amount
    return amount


def withdraw(amount):
    global bank_balance
    if amount > bank_balance:
        print("You can't do that!")
        return False

    else:
        bank_balance -= amount
        return amount


def check_balance():
    return global bank_balance

def run_main():
    print(
        f"Welcome to your bank account, your bank balance is: 0 $\nTo check your account click -- 1\nTo deposit click "
        f"--"
        f"2\nTo withdraw click -- 3\nTo exit at any stage click -- q")
    
    while True:
        action = input("What do you want to do? ")

        if action.lower() == "q":
            print("Goodbye!")
            quit()

        elif action == "1":
            print(f"Your balance is: {check_balance(bank_balance)}")

        elif action == "2":
            bank_balance = deposit(bank_balance)

        elif action == "3":
            bank_balance = withdraw(bank_balance)
            
        else:
            print("Only 1, 2, 3, or q")



