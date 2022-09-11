print("SUM FUNCTION EXAMPLE")
print("--------------------------")
nums = []
while True:
    num = int(input("Enter a number: "))
    nums.append(num)
    choice = input("Do you want to add more data? (y/n) ")
    if choice == "y":
        continue
    elif choice == "n":
        break
print("sum: {}".format(sum(nums)))
print("--------------------------")
print()
print("HEX FUNCTION EXAMPLE")
print("--------------------------")
num = int(input("Enter a number: "))
print("Hex code of {}: {}".format(num, hex(num)))
print("--------------------------")
