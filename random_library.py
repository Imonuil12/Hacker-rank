#PROBLEM NUMBER 37

#import random

#num = random.randint(0, 100)
#print(num)

#PROBLEM NUMBER 38
#import random

#fruit = random.choice(["apple", "bannana", "charry", "grapes", "lemon"])
#print(fruit)


#PROBLEM NUMBER 38

#Randomly choose either heads or tails (“h” or “t”). Ask
#the user to make their choice. If their choice is the same
#as the randomly selected value, display the message
#“You win”, otherwise display “Bad luck”. At the end, tell
#the user if the computer selected heads or tails.

#import random

#coin = random.choice(["head", "tails"])
#guess = input("Choose heads or tails: ")
#if guess == coin:
#    print("You win!")
#else:
#    print("Bad luck!")
#if coin == "head":
#    print("It was heads")
#else:
#    print("It was tails") 


#PROBLEM NUMBER 39

#Randomly choose a number between 1 and 5. Ask the user to pick a
#number. If they guess correctly, display the message “Well done”,
#otherwise tell them if they are too high or too low and ask them to pick a
#second number. If they guess correctly on their second guess, display
#“Correct”, otherwise display “You lose”.

#import random

#num = random.randint(1,5)

#guess = int(input("Pick a number between 1 and 5: "))

#if guess == num:
#    print("You win!")
#elif guess > num:
#    print("Too high!")
#    guess = int(input("Guess again: "))
#    if guess == num:
#        print("Correct!")
#    else:
#        print("You loose!")
#elif guess < num:
#    print("Too low!")
#    guess = int(input("Guess again: "))
#    if guess == num:
#        print("You win!")
#    else:
#        print("You loose!") 
#        
#print("The number was ", num)

#PROBLEM NUMBER 40

#Make a maths quiz that asks five questions by randomly
#generating two whole numbers to make the question
#(e.g. [num1] + [num2]). Ask the user to enter the
#answer. If they get it right add a point to their score. At
#the end of the quiz, tell them how many they got correct
#out of five.


#import random

#score = 0
#count = 0

#while count < 5:
#    num1 = random.randint(1, 1000)
#    print("Num1 is equal to: ", num1)
#    num2 = random.randint(1,1000)
#    print("Num2 is equal to: ", num2)
#    guess = int(input("What is the sum of num1 and num2? "))
#    if guess == num1+num2:
#        score = score +1
#    count = count+1
#    print("Your score is: ", score)

#Another solution

#score = 0

#for i in range(1,6):
#    num1 = random.randint(1,50)
#    num2 = random.randint(1,50)
#    print("num1 is equal to", num1, "and num2 is", num2)
#    guess = int(input("Enter the sum of num1 and num2: "))
#    if guess == num1+num2:
#        score = score + 1
#print("Your overall score is: ", score)

#PROBLEM NUMBER 41
#Display five colours and ask the user to pick one. If they
#pick the same as the program has chosen, say “Well
#done”, otherwise display a witty answer which involves
#the correct colour, e.g. “I bet you are GREEN with envy”
#or “You are probably feeling BLUE right now”. Ask
#them to guess again; if they have still not got it right,
#keep giving them the same clue and ask the user to
#enter a colour until they guess it correctly.

#import random

#colors = ["green", "blue", "red", "orange", "yellow"]
#print("The given colors are: ",colors)
#color = random.choice(colors)

#guess = input("Guess the color computer picked: ")

#while guess != color:
#    if color == "green":
#        guess = input("You might be feeling green today, try again: ")
#    elif color == "blue":
#        guess = input("You might be feeling blue today, try again: ")
#    elif color == "red":
#        guess = input("You might be feeling red today, try again: ")
#    elif color == "orange":
#        guess = input("You might be feeling orange today, try again: ")
#    else:
#        guess = input("You might be feeling yellow today, try again: ")
#if guess == color:
#    print("Well done!")
#    quit()

#Another solutions

#color = random.choice(["green", "blue", "red", "orange", "yellow"])
#theirchoice = True

#while theirchoice == True:
#    choice = input("Guess a color among green, blue, red, orange and yellow: ")
#    choice = choice.lower()
#    if choice == color:
#        print("Well done!")
#        theirchoice = False
#    else:
#        if color == "green":
#            print("I am feeling green today, guess again: ")
#        elif color == "blue":
#            print("I am feeling blue today, guess again: ")
#        elif color == "red":
#            print("I am feeling red today, guess again: ")
#        elif color == "orange":
#            print("I am feeling orange today, guess again: ")
#        elif color == "yellow":
#            print("I am feeling yellow today, guess again: ")
