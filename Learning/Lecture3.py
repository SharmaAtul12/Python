#  List In Python ----------------------------------------------------------------------------------------------

# Strings Are Immutable In Python But List and List Methods are Mutable (Inki Values Inside List change ke Ja Skti hh)

'''marks = [55, 59, 41, 22, 89]
# print(marks.sort()).return krega None Matlab Kuch Nhi(return nhi krta kuch).Ye Original List(marks) mm he change kar dega . So vhi print krani hh
print(marks) # Sorted List Mil Jayegi'''

'''fruits = ["banana", "litchi", "apple"]
fruits.sort() # Yha Acc to alphabets sorting hoti hh..
print(fruits)'''

# Tuples In Python 

# Tuple is Immutable in Python (Original Tuple Mm Koi Change Nhi Kar Skte) -----------------------------------------------
'''tupple = (45, 56, 59, 88, 100)
Single Value Tupple = tup = (5,) comma lga dete hh.agar Comma Nhi lgaya so Python 5 ko integer Samjega Instead of tupple'''

# Practice Questions ------------------------------------------------------------------------------------------->>>>>>>>>>>

# Q1. WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
'''
  movies = []
  a  = input("Enter the Name Of Your first Movie : ")
  b  = input("Enter the Name Of Your Second Movie : ")
  c  = input("Enter the Name Of Your Third Movie : ")
  movies.append(a)
  movies.append(b)
  movies.append(c)
  print(movies)
'''

# Q2. WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# 1. [1, 2, 3, 2, 1]       2. [1, "abc", "abc", "1"]
'''
  list1 = [1, 2, 3, 2, 1] 
  list2 = list1.copy()
  list2.reverse()
  if(list1 == list2):
      print("List Is Palindrom")
  else:
      print("List is Not pallindrom")
'''

# Q3. WAP to count the number of students with the “A” grade in the following tuple. ("C", "D", "A", "A","B", "B", "A")
'''
  tupple = ("C", "D", "A", "A","B", "B", "A")
  print(tupple.count("A"))
'''

# Q4. Store the above values in a list & sort them from “A” to “D”.Means In Ascending Order
'''
  list = ["C", "D", "A", "A","B", "B", "A"]
  list.sort()
  print(list)
'''


