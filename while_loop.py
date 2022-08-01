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

