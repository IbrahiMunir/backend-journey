# Tasks solution using conditional statments and compersion opretor 

#Task1

# Write a Python program that:
# Takes a number from the user and checks:
# If the number is positive, print "Positive"
# If the number is **negative, print "Negative"`
# Otherwise print "Zero"

userNum = int(input("Enter your number: "))

if userNum>0:
    print(f"Number is positive {userNum} ")
elif userNum<0:
    print(f"Number is negative {userNum}")
else:
    print(f"Number is zero {userNum}")


#Task2

# Write a Python program that:
# Takes two numbers from the user and prints the largest number using if-else.

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))

if num1>num2:
    print(f"{num1} is greater than num2 {num2}");
else:
    print(f"{num2} is greater than num1 {num1}")


#Task3
# Write a Python program that:
# Takes marks from the user
# First checks if the student passed or failed
# If the student passed, then check the grade using nested if

marks = int(input("Enter your marks: "))

if marks>=50:
    print("Student is passed")
    if(marks>=90):
         print("Grade A")
    elif(marks>=70):
        print("Grade B")
    else:
        print("Grade C")
else:
    print("Fail")


#Bonus MCQ (Test Yourself)
# Q: What will be the output?
# x = 10
# y = 20

# if x > y:
#     print("X is greater")
# else:
#print("Y is greater")

# output: Y is greater