# Q1 =>
# n = int(input("Enter a No : "))
# for i in range(n):
#     print("*"*n) 

# OUTPUT => 
# *****
# *****
# *****
# *****
# *****

# Q2 => 
# n = int(input("Enter a No : "))
# for i in range(n):
#     print("3"*n) 

# OUTPUT => 
# 333
# 333
# 333

# Q3 => 
# n = int(input("Enter a No : "))
# for i in range(n):
#     print(str(i+1)*n)

# OUTPUT => 
# 111
# 222
# 333

# Q4 => 
# n = int(input("Enter a No : "))
# for i in range(n):
#     print(chr(65)*n)

# OUTPUT => 
# AAAAA
# AAAAA
# AAAAA
# AAAAA
# AAAAA

# Q5 => 
# n = int(input("Enter a No : "))
# for i in range(n):
#     print(chr(65+i)*n)

# OUTPUT => 
# AAAAA
# BBBBB
# CCCCC
# DDDDD
# EEEEE

# Q6 => 
# n = int(input("Enter a No : "))
# for i in range(n):
#     for j in range(n):
#         print(j+1,end=" ")
#     print()

# OUTPUT => 
# Enter a No : 3
# 1 2 3 
# 1 2 3
# 1 2 3



# Q7=> 
# n = int(input("Enter a No : "))
# for i in range(n):
#     for j in range(n):
#         print(chr(65+j),end=" ")
#     print()

# OUTPUT => 
# Enter a No : 3
# A B C 
# A B C
# A B C

# Q8 => 

# n = int(input("Enter a No : "))
# word = 3
# for i in range(n): 
#     print(str(word)*n)
#     word -= 1

# OUTPUT => 
# Enter a No : 3
# 333
# 222
# 111

# Q9 => 
# n = int(input("Enter a No : "))
# for i in range(n):
#     word = 2
#     for j in range(n):
#         print(chr(65+word),end=" ")
#         word -= 1
#     print()

# OUTPUT => 
# Enter a No : 3
# C B A 
# C B A
# C B A

# Q10 => 

# n = int(input("Enter a No : "))
# for i in range(n):
#     print("*"*(n-i))

# OUTPUT => 
# Enter a No : 4
# ****
# ***
# **
# *

# Q11 => 

# n = int(input("Enter a No : "))
# for i in range(n):
#     print((" "*(n-i-1)) + "* "*(i+1))

# OUTPUT => 
# Enter a No : 3
#   * 
#  * *
# * * *

# Q12 =>

# n = int(input("Enter a No : "))
# for i in range(n): 
#     for j in range(n-i):
#         print(chr(65+j), end=" ")
#     print()

# OUTPUT => 
# Enter a No : 5
# A B C D E 
# A B C D
# A B C
# A B
# A

# Q13 => 

# n = int(input("Enter a No : "))
# for i in range(n):
#     print((" "*(i)) + "* "*(n-i))

# OUTPUT => 
# Enter a No : 3
# * * * 
#  * *
#   *

# Q14 => 
# n = int(input("Enter a No of rows : "))

# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
        
# for i in range(n-1,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# OUTPUT => 
# Enter a No of rows : 5
# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *



