mark1 = int(input("Enter Mark 1 "))
mark2 = int(input("Enter Mark 2 "))
mark3 = int(input("Enter Mark 3 "))
mark4 = int(input("Enter Mark 4 "))
mark5 = int(input("Enter Mark 5 "))
mark6 = int(input("Enter Mark 6 "))
mark7 = int(input("Enter Mark 7 "))
mark8 = int(input("Enter Mark 8 "))
mark9 = int(input("Enter Mark 9 "))
mark10 = int(input("Enter Mark 10 "))

sum = mark1 + mark2 + mark3 + mark4 + mark5 + mark6 + mark7 + mark8 + mark9 + mark10
average = sum / 10

minimum = min(mark1,mark2,mark3,mark4,mark5,mark6,mark7,mark8,mark9,mark10)
maximum = max(mark1,mark2,mark3,mark4,mark5,mark6,mark7,mark8,mark9,mark10)

print ("Minimum Mark is ", minimum)
print ("Maximum Mark is ", maximum)
print ("Average of the Marks is ", average)