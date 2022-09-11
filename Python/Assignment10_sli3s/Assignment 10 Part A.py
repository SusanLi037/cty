#Programmer name: Susan Li
#Program creation date: September 1, 2022

#Data science tool

#list of numbers
nums = []
#loop until user doesn't want to add mroe data
while True:
    #ask user to enter an integer value
    num = input("Please enter an integer value ")
    #if user doesn't enter an integer value
    if str.isdigit(num) == False:
        print("{} is not an integer".format(num))
        #ask user to enter a valid integer value
        num2 = int(input("Please enter a valid integer value "))
        #add the integer to the list
        nums.append(num2)
    #if user did enter an integer value
    elif str.isdigit(num) == True:
        num = int(num)
        #add the integer to the list
        nums.append(num)
    #ask if user wants to add more data
    choice = input("Do you want to add more data? y/n ")
    #continue
    if choice == "y":
        continue
    #stop the loop
    if choice == "n":
        break
#Print data summary 
print()
print("Data Summary")
print("-------------")
#print the number of numbers
print("Number of data: {}".format(len(nums)))
#print the minimum number
print("Minimum: {}".format(min(nums)))
#print the maximum number
print("Maximum: {}".format(max(nums)))
#calculate and print the range
print("Range: {}".format(max(nums) - min(nums)))
#calculate and print the average
print("Average: {}".format((sum(nums))/len(nums)))
