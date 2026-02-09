#  Practice Questions ---------------------------------------------------------------

# Q1. Store following word meanings in a python dictionary :
# table : “a piece of furniture”, “list of facts & figures”
# cat : “a small animal”
'''
  word_meaning = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
  }

  print(word_meaning)
'''

# Q2. You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# ”python”, “java”, “C++”, “python”, “javascript”,“java”, “python”, “java”, “C++”, “C”
'''
  subject_set = {"python", "Java", "C++", "python", "JavaScript", "Java", "python","Java","C++", "C"}
  print("Total Classroom Required = ", len(subject_set))
'''

# Q3. WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#     an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}
'''
  marks = {}
  physics_marks = int(input("Enter Marks of Physics : "))
  marks.update({"physics" : physics_marks})
  chemistry_marks = int(input("Enter Marks of chemistry : "))
  marks.update({"chemistry" : chemistry_marks})
  Maths_marks = int(input("Enter Marks of Maths : "))
  marks.update({"Maths" : Maths_marks})

  print(marks)
'''

# Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built-in data types) 

# 1st method =>
# values = {9,"9.0"} # Kisi Bhi Ek Value Ko String ke Form mm Add kr diya So 9 And 9.0 alag Alg mana jayega ..

# 2nd Method =>
'''
  values = {
    ("flaot", 9.0),
    ("int", 9)
  }
  print(values)
'''
