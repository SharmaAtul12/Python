 
# Q1. LCM OF TWO NUMBERS =>

# def lcm(a,b):
#     if a>b:
#         greater = a
#     else:
#         greater = b

#     while True:
#         if greater % a == 0 and greater % b == 0:
#             lcm = greater
#             break
#         greater += 1
#     return lcm
    
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# result = lcm(a,b)
# print("Result : ", result)


# Q2. Reversing A String =>

# a = input("Enter The String : ")
# rev_str = " "
# for ch in a:
#     rev_str = ch + rev_str
# print(rev_str) 

# Using Built In Function =>
# a = input("Enter The String : ")
# rev_str = a[::-1]
# print(rev_str)

# Q3. Count The Frequency Of Character In A String =>

# str = input("Enter The String : ")
# freq = {}

# for ch in str:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# print(freq)

# Q4. Count The No Of Vowels In A String =>

# str = "Atul Sharma Eiout"
# vowels = "a","e","i","o","u","A","E","I","O","U"

# count = 0
# for ch in str:
#     if ch in vowels:
#         count += 1
# print("Total Number Of Vowels In String => ", count)



# Q5. WAP To Print Whether The Number Is Prime Or Not =>

# num = int(input("Enter Number : "))
# count = 0
# for i in range(1, num+1):
#     if num % i == 0:
#         count += 1
# if count == 2:
#     print("Prime No")
# else: 
#     print("Not Prime")

# Q6. WAP To Print All Prime Numbers Till n =>

# n = int(input("Enter n : "))
# for num in range(2,n+1):
#     count = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             count+= 1
#     if count == 2:
#         print(num, "Is Prime")
#     else:
#         print(num, "is Not Prime")

# Q7. generalized Python program to check whether a number is an Armstrong number =>

# num = int(input("Enter No To Check : "))
# order = len(str(num))

# sum = 0
# temp = num

# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit**order
#     temp = temp // 10

# if sum == num:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")


# Q8. Python program to check if a year is a leap year:

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")



# Q9.  Python Code to Check Fibonacci Number 

# num = int(input("Enter a num: "))
# a,b = 0,1
# while b<num:       # 	Generates Fibonacci numbers until b reaches or crosses num
#     a,b = b, a+b
# if num == 0 or b == num:   # Checks if the number is 0 or matched exactly in the sequence
#     print(num, "Is Fibonacci Number")
# else :
#     print(num, "Is Not Fibonacci Number") 



# Q10.  Python Code to Generate Fibonacci Series

# n = int(input("Enter a num: "))
# a,b = 0,1 
# count = 0

# while count<n:
#     print(a, end=" ")
#     a,b = b,a+b
#     count += 1


# Q11. Wap that Accepts Sentence And Calculates the No Of Digits , uppercase and lowercase . 

# sentence = input("Enter The Sentence : ")
# digits = upper = lower = 0

# for ch in sentence:
#     if ch.isdigit():
#         digits+=1
#     elif ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1

# print("Digits : ", digits)
# print("Uppercase : ", upper)
# print("Lowercase : ", lower)

# Q12 . Write a Python program to print factorial of a given number.

# n = int(input("enter your no : "))
# a = n
# fact = 1

# if n == 0 or n == 1:
#     print("Factorial is 1")
# else:
#     while(n>1):
#         fact = fact*n
#         n -= 1
# print("The Factorial Of: ",a,"Is => ",fact)

