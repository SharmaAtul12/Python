
# FUNCTIONS =======================================>
# PRACTICE QUESTIONS -->

# Q1. WAF to print the length of a list. ( list is the parameter)
'''
players = ["Rohit", "Kohli", "Dhoni", "Iyer"]

def print_len_players(list):
    print(len(list))

print_len_players(players)
'''

# Q2. WAF to print the elements of a list in a single line. ( list is the parameter)
'''
players = ["Rohit", "Kohli", "Dhoni", "Iyer", "Pant", "Pooran"]

def print_players(list):
    for item in list:
        print(item, end=" ")

print_players(players)
'''

# Q3. WAF to find the factorial of n. (n is the parameter)
'''
def cal_fac(n):
    i = 1
    fac = 1
    while i<=n:
        fac = fac*i
        i +=  1
    return fac
    

x = cal_fac(5)
print(x)
'''

# Q4. WAF to convert USD to INR.
'''
def convert(usd):
    inr = usd*83
    print(usd,"USD = ",inr,"INR")

convert(1)
convert(2)
convert(3)
convert(4)
convert(5)
'''

# RECURSION QUESTIONS ================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q1. Write a recursive function to calculate the sum of first n natural numbers.
'''
def calc_sum(n):
    if(n==0):     # Base Case
        return 0
    return calc_sum(n-1) + n

print(calc_sum(5))
'''

# Q2. Write a recursive function to print all elements in a list. Hint : use list & index as parameters.

list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

def print_list(list,index=0):  #Index ke default value 0 mani jayegi , agar function call mm pass nhi kri hh..
    if(index == len(list)): # Base Case
        return
    print(list[index])
    print_list(list,index+1)

print_list(list)
    
