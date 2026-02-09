# WHILE LOOP QUESTIONS =>>>>>>>>>>>>>>>>>>>>>>>>>

# Q1. Print numbers from 1 to 100.
'''
  num = 1
while num <= 100 : 
    print(num)
    num += 1
'''

# Q2. Print numbers from 100 to 1
'''
  num = 100
while num >= 1 : 
    print(num)
    num -= 1
'''

# Q3. Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

'''
  list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
  i = 0
  while i<= len(list) :
    print(list[i])
    i += 1
'''

# Q4. Print the multiplication table of a number n.
'''
  n = int(input("Enter The Number To get The Table Of That : "))
  count = 1
  while count <= 10 :
    print(n*count)
    count +=1
'''

# Q5. Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
'''
tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = int(input("Enter The Number To Find In The Tuple : "))
count = 0
while count < len(tuple) :
    if(tuple[count] == x):
        print("Your Entered Number Is Present In Tuple at index ", count)
    count += 1
'''
# FOR LOOP ==>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
tuple = (1,2,3,4,5,6,7,8,9,10)
for val in tuple: # tuple ke ek ek value "val" mm jayega and print hoti jayegi . index+ for loop apne aap manage kr lega.
    print(val)
'''

# Practice Questions =>>>>

# Q1. Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
'''
list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for num in list:
    print(num)
'''

# Q2. Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
'''
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = int(input("Enter Number To Search : "))
idx = 0
for val in tup:
    if(val == x):
        print("Number Found at ",idx)
    idx += 1
'''

# using for & range( ) =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q1. Print numbers from 1 to 100.
'''
for i in range(1,101):
    print(i)
'''

# Q2. Print numbers from 100 to 1.
'''
for i in range(100,0,-1):
    print(i)
'''

# Q3. Print the multiplication table of a number n.
# Method 1 =>
''' 
n = int(input("Enter Number To Get Table Of It : "))
for i in range(n,n*10+1,n):
    print(i)
'''

# Method 2 =>
'''
n = int(input("Enter Number To Get Table Of It : "))
for i in range(1,11):
    print(n*i)
'''

# Pass Statement And Some More Questions => 
'''
for i in range(5):
    pass

print("Pass Statement uses When Loop ss kuch Kam Nhi krana . In Future krana h . so its acts as placeholder")
'''

# Q1. WAP to find the sum of first n natural numbers. (using while)
'''
n = int(input("Enter Value To get Sum Upto It : "))
i = 1
sum = 0
while i<=n:
    sum = sum + i
    i += 1
print("Sum Is : ",sum)
'''


# WAP to find the factorial of first n numbers. (using for)
'''
n = int(input("Enter Value To Calculate Factorial : "))
i = 1
fac = 1
while i<=n:
    fac = fac*i
    i += 1
print("Factorial Is : ",fac)
'''