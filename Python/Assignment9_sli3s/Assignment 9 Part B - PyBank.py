#Programmer name: Susan Li
#Program creation date: August 28, 2022

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
print("------------------")
print("------------------")
print(" ")


#User interaction

#Log in or create new account
log_in = input('''Press 1 to LOG IN...
Press 2 to CREATE NEW ACCOUNT...
''')
account = {}
if log_in == "2":
    #set balance to $0
    balance = 0.0
    #Enter your name
    name = input("Enter your name: ")
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
            account[name] = balance
            break;
elif log_in == "1":
    name = input("Enter your name: ")
    balance = account[name]
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
            account[name] = balance
            break;
