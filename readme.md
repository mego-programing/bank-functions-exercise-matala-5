# Bank Interface Exercise
In this exercise, you will be implementing a simple bank interface in Python.

## Instructions

1. Clone this repository to your local machine.
2. Implement the bank interface according to the specifications provided below.
3. Commit your changes and push them to your GitHub repository.
4. If you're stuck or need clarification, feel free to reach out for help.

## Bank Interface Specifications
- Create a balance variable
- Create the following functions:
   - `deposit(amount)` - adds the amount to the `balance` variable
   - `withdraw(amount)` - withdrawing the amount from the `balance` variable if the withdraw amount is more than the balance amount - return `False`
   - `check_balance()` - returns the bank balance

### Your bank interface should have the following functionalities:
1. Display a menu with options for users:
    - Check balance
    - Deposit funds
    - Withdraw funds
    - Exit

2. Users should be able to:
    - Check their balance, which should initially be 0.
    - Deposit funds into their account.
    - Withdraw funds from their account (cannot withdraw more than the current balance).
    - Exit the program.
3. Ensure your code is well-structured and easy to understand.