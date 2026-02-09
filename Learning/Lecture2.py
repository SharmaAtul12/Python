# If Else Statement ..........................................................................................
''' If Statements Sari Check Hoti hh 
 But elif Tab he check hogi Jab If condition False hh.
 else Statement Is Executed when all the above conditions are false''' 
'''
Example => 
    marks = 55
    if(marks >= 90):
        print("Grade A") # 4 spaces ke bdd print function likhna hh This Is called Identation In python..
    elif(marks >= 80 and marks < 90):
        print("Grade B")
    elif(marks >=70 and marks < 80):
        print("Grade C")
    else:
        print("Grade D")
'''

# Practice  ------------------------------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q1. WAP to input user’s first name & print its length.

'''name = input("Enter Your Name : ")
print("Length Of Your Name Is :",len(name))'''

# Q2. WAP to find the occurrence of ‘$’ in a String. 

'''str = "Hello$ It Is a dollar$ Sign"
print("No Of Dollars In Str Is :", str.count("$"));'''

# Q3. WAP to check if a number entered by the user is odd or even.
'''num = int(input("Please Enter Any Number To Check Whether It Is Even or odd : "))
if(num % 2 == 0):
    print("Even")
else:
    print("Odd")'''

# Q4. WAP to find the greatest of 3 numbers entered by the user.

'''a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
if(a>b and a>c):
    print(a," Is the Greatest Number")
elif(b>a and b>c):
    print(b," Is the Greatest Number")
else:
    print(c," Is the Greatest Number")'''

# Q5. WAP to check if a number is a multiple of 7 or not.

'''num = int(input("Please Enter Any Number To Check Whether It Is Multiple Of 7 or Not : "))
if(num % 7 == 0):
    print(num,"Is a Multiple Of 7")
else:
    print(num,"Is Not a Multiple Of 7'''

