import random
score = 0
playing = True
while (playing):
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    operator = random.choice(["+", "-", "*", "/"])
    if operator == "+":
        print(num1, "+", num2, "= ")
        answer = int(input())
        if answer == num1 + num2:
            print("correct")
            score = score + 1
        elif answer != num1 + num2:
            print("wrong")
            score = score
    elif operator == "-":
        print(num1, "-", num2, "= ")
        answer = int(input())
        if answer == num1 - num2:
            print("correct")
            score = score + 1
        elif answer != num1 - num2:
            print("wrong")
            score = score
    elif operator == "*":
        print(num1, "*", num2, "= ")
        answer = int(input())
        if answer == num1 * num2:
            print("correct")
            score = score + 1
        elif answer != num1 * num2:
            print("wrong")
            score = score
    elif operator == "/":
        if num1 > num2:
            print(num1, "/", num2, "= ")
            answer = float(input())
            if answer == num1 / num2:
                print("correct")
                score = score + 1
            elif answer != num1 / num2:
                print("wrong")
                score = score
        elif num1 < num2:
            print(num2, "/", num1, "= ")
            answer = float(input())
            if answer == num2 / num1:
                print("correct")
                score = score + 1
            elif answer != num2 / num1:
                print("wrong")
        else:
            print(num1, "/", num2, "= ")
            answer = int(input())
            if answer == num1 / num2:
                print("correct")
                score = score + 1
            elif answer != num1 / num2:
                print("wrong")
                score = score
    end = input("Do you want to continue? (yes/no) ")
    if end == "no" or end == "No" or end == "NO" or end == "n" or end == "N":
        print("Score: {}".format(score))
        print("Thanks for playing!")
        playing = False
        break;
    elif end == "yes" or end == "Yes" or end == "YES" or end == "y" or end == "Y":
        playing = True
