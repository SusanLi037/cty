#Programmer name: Susan Li
#Program creation date: August 21, 2022

#Get 10 random numbers from one to 25, then add up the even numbers and the odd numbers

#import random module
import random
#define variables
sum_even = 0
sum_odd = 0
#print "Random Integers" on the screen
print("Random Integers")
#loop 10 times
for i in range(0, 10):
    #pick a random number between 1 and 25 and print the number on the screen
    num = random.randint(1, 25)
    print(num)
    #add the even numbers
    if num % 2 == 0:
        sum_even = sum_even + num
    #add the odd numbers
    elif num % 2 == 1:
        sum_odd = sum_odd + num
#print the sums on the screen
print("Sum of even integers: {}".format(sum_even))
print("Sum of odd integers: {}".format(sum_odd))
