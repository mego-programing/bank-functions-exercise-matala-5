balance = 0


#
def deposit(amount):
    global balance
    balance += amount


#
def withdraw(amount):
    global balance
    balance -= amount

    # checks if the withdrawal is greater than the balance
    if amount > balance:
        return False


def check_balance():
    global balance
    return balance


def menu():
    user = int(
        input(
            "press 1 to deposit \n press 2 to withdraw money \n press 3 to check balance"
        )
    )

    if user == 1:
        user1 = int(input("What is the deposit amount? "))
    elif user == 2:
        user2 = int(input("What is the withdrawal amount? "))
    elif user == 3:
        user2 = int(
            input(
                "Your balance is",
            )
        )
