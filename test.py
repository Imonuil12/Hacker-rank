#Iterate the given list of numbers
# and print only those numbers which are divisible by 5

list = [10, 20, 33, 46, 55]

x = len(list)

for n in range(0, x):
    if list[n] % 5 == 0:
        print(list[n])
    else:
        print("No divisable by 5")
