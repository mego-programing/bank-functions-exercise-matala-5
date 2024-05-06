bank_balance = 0


def deposit(amount):
    deposit_amount = float(input("How much money do you want to deposit? "))
    amount += deposit_amount
    return amount


def withdraw(amount):
    withdrawal_amount = float(input("How much money do you want to withdraw? "))
    if withdrawal_amount > amount:
        print("You can't do that!")
        return False

    else:
        amount -= withdrawal_amount
        return amount


def check_balance(amount):
    return amount


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



