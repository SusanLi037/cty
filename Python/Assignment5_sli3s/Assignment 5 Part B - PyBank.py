#Programmer name: Susan Li
#Program creation date: August 15, 2022

#PyBank app

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
#customer name and balance function
def customer_name_and_balance():
    print("Customer name: {}".format(name))
    print("Balance: ${}".format(balance))
    print(" ")
#print customer name and balance
customer_name_and_balance()
#deposit amount function
def deposit(balance, deposit_amount):
    return(balance + deposit_amount)
balance = deposit(balance, float(input("Enter the deposit amount: ")))
#print customer name and balance
customer_name_and_balance()
#withdrawal amount function
def withdrawal(balance, withdrawal_amount):
    return(balance - withdrawal_amount)
balance = withdrawal(balance, float(input("Enter the withdrawal amount: ")))
#print customer name and balance
customer_name_and_balance()
