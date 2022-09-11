#Programmer name: Susan Li
#Program creation date: August 27, 2022

#Sort a list of numbers

nums = []
while True:
    num = int(input("Please enter a number "))
    nums.append(num)
    choice = input("Do you want to add more data? (y/n) ")
    if choice == "y":
        continue
    elif choice == "n":
        print()
        print("Original list: {}".format(nums))
        print("Sorting...")
        nums.sort()
        print("Sorted list: {}".format(nums))
        break
