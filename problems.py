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