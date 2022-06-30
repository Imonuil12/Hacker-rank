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


