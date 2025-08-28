#. Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?

a = int(input("Enter the number: "))
if a % 2 == 0:
    print("even no.: ",a)
else :
    print("not even")