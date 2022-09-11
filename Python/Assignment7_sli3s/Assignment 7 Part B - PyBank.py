#Programmer name: Susan Li
#Program creation date: August 21, 2022

#PyBank app

#function for printing the costomer name and balance
def customer_name_and_balance(name, balance):
    print("Customer name: {}".format(name))
    print("Balance: ${}".format(balance))
    print(" ")
#deposit function
def deposit(balance, deposit_amount):
    return(balance + deposit_amount)
#withdrawal function
def withdrawal(balance, withdrawal_amount):
    #check for overdraft
    if balance - withdrawal_amount < 0:
        print("You have withdrawn more money than your bank account has, which would result in a negative account balance. You will not be able to take ${} out of your account.".format(withdrawal_amount))
        balance == balance
        return balance
    elif balance - withdrawal_amount > 0:
        return(balance - withdrawal_amount)
#choice menu function
def choices():
    #ask user to choose to make a deposit, make a withdrawal, or quit
    print('''Press 1 to make a deposit
Press 2 to make a withdrawal
Press 9 to quit''')
    choice = input()
    return choice

#Introduce PyBank
print("Welcome to PyBank")
print("Your one stop online Banking App!")
print(" ")
print("------------------")
print(" ")

#User interaction

#Enter your name
name = input("Enter your name: ")
#set balance to $0
balance = 0.0
#print customer name and balance
customer_name_and_balance(name, balance)
while True:
    choice = choices()
    #make a deposit
    if choice == "1":
        #prompt user for deposit amount
        balance = deposit(balance, float(input("Enter the deposit amount: ")))
        #print customer name and balance
        customer_name_and_balance(name, balance)
    #make a withdrawal
    if choice == "2":
        #prompt user for withdrawal amount
        balance = withdrawal(balance, float(input("Enter the withdrawal amount: ")))
        #print customer name and balance
        customer_name_and_balance(name, balance)
    #quit
    if choice == "9":
        break;
