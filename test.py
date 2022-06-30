#Write a function to return True if the first and last number of 
# a given list is same. If numbers are different then return False.


numbers_x = [6,2,3,4,5,6]

numbers_y = [5,6,7,8,9,1]

x = numbers_x
y = numbers_y

xcount = len(numbers_x)
ycount = len(numbers_y)


print("Given list: ", x)

if x[0] == x[xcount-1]:
    print("True!")
else:
    print("False!")
    
print("Given list: ", y)
    
if y[0] == y[ycount-1]:
    print("True!")
else:
    print("False!")