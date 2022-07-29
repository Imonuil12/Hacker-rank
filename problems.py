import math
import os
import random
import re
import sys

n = input("Please enter an integer in the range from 1 to 100: ")

# Check if n is an integer and in the range
if n.isdigit():
    n = int(n)
    
    if n < 1 or n > 100:
        print("It is out of range, please try another time!")
        quit()
        
# If a letter is typed, the game quits
else:
    print("Print a number next time!")
    quit()
#If n is odd, print Weird
if n % 2 != 0:
    print("Weird")
#If n is even and in the inclusive range of 2 to 5, print Not Weird
elif n >= 2 and n <= 5:
    print("Not Weird")
#If n is even and in the inclusive range of 6 to 20, print Weird
elif n >= 6 and n <= 20:
    print("Weird")
#If n is even and greater than 20, print Not Weird
elif n > 20:
    print("Not Weird")
else:
    print(n)

# The easy alternative solution

# n = int(input())
# if n % 2 == 1:
#   print("Weird")
# elif n % 2 == 0 and 2 <= n <= 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")
# else:
#     print("Not Weird") 
    
# Problem number 2

#a = input()
#b = input()

#Sum of a and b
#print(a + b)

#The difference of a and b
#print(a - b)

#The product of a and b
#print(a*b)

#PROBLEM NUMBER 4
#The provided code stub reads and integer, , from STDIN. For all non-negative integers i<n , print i^2.

#Example

#The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

#0
#1
#4

#i = int(input("Please type a number: "))

#if i in range(1,21):
 #   for i in range(1, i):
 #       print(i * i)
#else:
#    print("Out of range!")



#PROBLEM NUMBER FIVE
#n = int(input("Here: "))

#if n in range(1, 151):
#    for n in range(1, n+1):
#        print(n)
#else:
#    print("Out of range!")


#PROBLEM NUMBER SIX

#a = int(input("enter a: "))
#b = int(input("enter b: "))

#if a*b <= 1000:
 #   print(a*b)
#else:
#    print(a+b)


#PROBLEM NUMBER 7

# loop from 1 to 10
#for i in range(0, 11):
    #x_sum = previous_num + i
    #print("Current Number", i, "Previous Number ", previous_num, " Sum: ", previous_num + i)
    # modify previous number
    # set it to the current number
    #previous_num = i
    
    
    
    
#PROBLEM NUMBER 8
#Write a program to accept a string from the user 
# and display characters that are present at an even index number.




#word = input("Type: ")

#print("Origional string is: ", word)

#size = len(word)

#for i in range(0, size -1, 2):
#    print("idex [", i, "]", word[i], end=", ")





#PROBLEM NUMBER 9

#word = input("Type: ")

#n = int(input("From which index to print? "))

#x = len(word)
#print("The origional word is: ", word)

#if n > x:
 #   print("The index is bigger than the word. Try one more time.")
    
#else:
  #  print("The word from index is: ")
 #   for n in range(n, x):
#        print(word[n], end="")

#Second way
#def remove_chars(word, n):
 #   print('Original string:', word)
  #  x = word[n:]
   # return x

#print("Removing characters from a string")
#rint(remove_chars("hellpooo", 4))


#PROBLEM NUMBER 10

#Write a function to return True if the first and last number of 
# a given list is same. If numbers are different then return False.


#numbers_x = [6,2,3,4,5,6]

#numbers_y = [5,6,7,8,9,1]

#x = numbers_x
#y = numbers_y

#xcount = len(numbers_x)
#ycount = len(numbers_y)


#print("Given list: ", x)

#if x[0] == x[xcount-1]:
 #   print("True!")
#else:
 #   print("False!")
    
#print("Given list: ", y)
    
#if y[0] == y[ycount-1]:
 #   print("True!")
#else:
 #   print("False!")


#PROBLEM NUMBER 11

#Write a program to find how many times substring “Emma” appears in the given string.

#str_x = "Emma is good developer. Emma is a writer"

#print(str_x.split())

#print(str_x.split().count("Emma"))




#PROBLEM NUMBER 12
#Write a program to find how many times substring “Emma” appears in the given string.

#from timeit import repeat


#user = input("Type any string: ")


#split_user = user.split()
#print(split_user)

#for i in split_user:
 #   print("The word ",i," in this string repeats: ",user.count(i), "times.")
 
 
 
 #PROBLEM NUMBER 13
 #Print the following pattern
#for x in range(10):
 #   for i in range(x):
  #      print(x, end=" ")
   # print("\n")
   
   
   
   
#PROBLEM NUMBER 14

#Write a program to check if the given number is a palindrome number.

#A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

#def palindrome(number):
    #print("original number", number)
   # original_num = number
    
    # reverse the given number
    #reverse_num = 0
   # while number:
       # reminder = number % 10
      #  reverse_num = (reverse_num * 10) + reminder
     #   number = number // 10

    # check numbers
    #if original_num == reverse_num:
   #     print("Given number palindrome")
  #  else:
 #       print("Given number is not palindrome")

#palindrome(111)
#palindrome(125)








#PROBLEM NUMBER 15

#name = input("Enter your name: ")

#print(len(name))\


#name = input("Enter your name: ")
#surname = input("Enter your surname: ")

#together = name + surname
#length = len(together)
#print(name, surname,".", "The length is equal to:",length)





#PROBLEM NUMBER 16

#name = input("Enter your name in lower case: ")
#surname = input("Enter your surname in lower case: ")

#iteled_name = name.title()
#titeled_surname = surname.title()

#print(titeled_name, titeled_surname)






#PROBLEM NUMBER 17

#line = input("Enter the first line of nurse rhyme: ")

#length = len(line)
#print(length)

#starting_number = int(input("What is the starting number? "))
#ending_number = int(input("What is the ending number? "))

#print(line[starting_number:ending_number])





#PROBLEM NUMBER 18
#import math
#number = float(input("Type a number larger than 500: "))

#squareroot = math.sqrt(number)

#print(round(squareroot, 2))



#PROBLEM NUMBER 19
#import math

#radius = float(input("Enter readius length: "))

#area = radius**2 * math.pi
#print(area)


#PROBLEM 20

#number1 = int(input("Enter the 1st number: "))
#number2 = int(input("Enter the 2nd number: "))

#remainder = number1 % number2

#devision = number1 // number2

#print(number1, "devided by", number2, "is equal to", devision, "with remaining", remainder)




#PROBLEM NUMBER 21

#import math
#print("1) Square \n2) Triangle")

#number = int(input("Enter a number: "))

#if number == 1:
   # side_number = int(input("Enter one side: "))
  #  area = side_number**2
 #   print("Area is equal to:", area)
#elif number == 2:
    #side = int(input("Enter the triangle side: "))
   # height = int(input("Enter the triangle height: "))
  #  area = (1/2) * side * height
 #   print("The triangle area is equal to: ", area)
#else:
    #print("Sorry you typed something wrong!")
    
    
    
#PROBLEM NUMBER 22
#name = input("Enter your name: ")
#number = int(input("How many times? "))
#for i in range(0, number):
#    print(name)




#PROBLEM NUMBER 23

#name = input("Enter your name: ")
#number = int(input("Enter number: "))

#for x in range(0,number):
    #for i in name:
        #print(i)
        
        
#PROBLEM NUMBER 24

#number = int(input("Enter a number between 1 and 12: "))

#if number in range(0,13):
#    for i in range(0, number):
#        print(i, "x", number, "=", i*number)
#else:
#    print("Out of range")



#PROBLEM NUMBER 25

#name = input("Enter your name: ")
#number = int(input("Enter a number: "))

#if number < 10:
#    for i in range(0,number):
#        print(name)
#else:
    #for i in range(0,3):
        #print("Too high!")
        
        
#PROBLEM NUMBER 26

#number = int(input("Enter a number: "))

#if number < 50:
#    for i in range (50, number-1, -1):
#        print(i)


#PROBLEM NUMBER 27
#total = 0
#repetition = 0

#while repetition <=5:
    #number = int(input("Enter a number: "))

    #question = input("Do you want the number to be added to the total? ")

    #if question == "yes":
   #     print(number+total)
    #else:
    #    print(total)
    
   # total = total + number
   
   
   #Another solution
   #total = 0

#for i in range(0,5):
#    num = int(input("Enter a number: "))
#    ans = input("Do you want to keep this number? ")
#    if ans == "yes":
#        total = total + num
#print(total)



#PROBLEM NUMBER 28
#direction = input("enter the direction (up or down): ")

#if direction == "up":
   # number_up = int(input("Enter till which number to count? "))
  #  for i in range(0,number_up+1):
 #       print(i)
#elif direction == "down":
    #number_down = int(input("Enter till which number to count down from 20? "))
    #for i in range(20, number_down-1, -1):
      #  print(i)   
      
      
#PROBLEM NUMBER 29

#number = int(input("How many people do you want to invite? "))

#if number < 10:
#    for i in range(1,number+1):
#        name = input("Enter the name of the person: ")
#        print(name, "has been invited.")
#else:
   # print("Too many people!")
   



#PROBLEM 30

#number = 0

#while number < 50:
    #num = int(input("Enter a random number: "))
    #number = num + number
    #print(number)
    
    
    
#PROBLEM NUMBER 31

#num = 0
#while num <= 5:
 #   num = int(input("Enter a random number: "))
#print("The last number you entered was", num)




#PROBLEM NUMBER 32

#    Ask the user to enter a
#number and then enter
#another number. Add these
#two numbers together and
#then ask if they want to add
#another number. If they
#enter “y", ask them to enter
#another number and keep
#adding numbers until they
#do not answer “y”. Once the
#loop has stopped, display
#the total.

#num1 = int(input("Enter a number: "))

#total = num1

#again = "y"

#while again == "y":
#        num2 = int(input("Enter another number: "))
#        total = num1 + num2
#        again = input("Do you want to add another number? ")
#print("The total is ", total)



#PROBLEM NUMBER 33

#count = 0
#name = input("Who do you want to invite to party? ")
#print(name, "has now been invited!")
#count = count + 1
#invite = "y"
#invite = input("Do you want to invite someone else? ")

#while invite == "y":
#    name1 = input("Who else? ")
#    count = count + 1
#    print(name1, "has been invited as well!")
#    invite = input("Do you want to invite someone else? ")
#print(count, "people have been invited!")

#Second way
#again = "y"
#count = 0

#while again == "y":
#    name = input("Who do you want to invite to party? ")
#    count = count +1
#    again = input("Do you want to invite someone else? ")
#print("You have", count, "people coming to your party!")


#PROBLEM NUMBER 34

#compnum = 50

#count = 0

#guess = int(input("Guess the number: "))

#while guess != compnum:
#    if guess < compnum:
#        print("Too low")
#        guess = int(input("Guess the number: "))
#        count = count +1
#    elif guess > compnum:
#        print("Too high")
#        guess = int(input("Guess the number: "))
#        count = count +1
#print("You got it! It took you", count, "guesses.")
        
#Another way

#compnum = 50
#count =1
#guess = int(input("Guess the number: "))

#while guess != compnum:
  #  if guess < compnum:
  #      print("Too low!")
 #   else:
 #       print("Too high!")
 #   count = count + 1
#    guess = int(input("Have another guess: "))
#print("Well done! You guessed it in", count, "tries.")


#PROBLEM NUMBER 35

#number = int(input('Please enter a number between 10 and 20: '))

#if number < 10:
#    print("Too low!")
#elif number > 20:
#    print("Too high!")
#else:
#    print("Thank you!")
#number = int(input('Try one more time: '))

#Another solution

#number = int(input("Enter a number between 10 and 20: "))

#while number < 10 or number > 20:
#    if number <10:
#        print("Too low!")
#    else:
#        print("Too high!")
#    number = int(input("Try one more time! "))
#print("Thank you!")


#PROBLEM NUMBER 36

#Using the song “10 green bottles”, display the lines “There are [num] green bottles
#hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle
#should accidentally fall”. Then ask the question “how many green bottles will be
#hanging on the wall?” If the user answers correctly, display the message “There will be
#[num] green bottles hanging on the wall”. If they answer incorrectly, display the
#message “No, try again” until they get it right. When the number of green bottles gets
#down to 0, display the message “There are no more green bottles hanging on the wall”.

#num = 10
#while num > 0:
#    print("There are", num, "green bottles hanging on the wall!")
#    print(num, "green bottles hanging on the wall!")
#    print("And if 1 green bottle should accedentally fall, ")
#    num = num - 1
#    answer = int(input("How many bottles will be hanging on the wall? "))
#    if answer == num:
#        print("There will be", num, "green bottles hanging on the wall.")
#    else:
#        while answer != num:
#            answer = int(input("No, try again: "))
#print("There will be", num, "green bottles hanging on the wall.")

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

#number = random.randint(1,5)
#choice = input("Guess a number between 1 and 5: ")

#if choice == number:
#    print("You win!")
#else:
#    print("You loose!")
    
#print("Computer chose", number)