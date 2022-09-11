#Programmer name: Susan Li
# Program creation date: August 7, 2022

#PyBank App - User Interaction

#Enter your name
name = input("Enter your name: ")
#set balance to $0
balance = 0.0
#print customer name and balance
print("Customer name: {}".format(name))
print("Balance: ${}".format(balance))
print(" ")
#Enter deposit amount and change the balance 
deposit_amount = int(input("Enter the deposit amount: "))
balance = balance + deposit_amount
#print customer name and balance
print("Customer name: {}".format(name))
print("Balance: ${}".format(balance))
print(" ")
#Enter withdrawal amount and change the balance
withdrawal_amount = int(input("Enter the withdrawal amout: "))
balance = balance - withdrawal_amount
#print customer name and balance
print("Customer name: {}".format(name))
print("Balance: ${}".format(balance))
