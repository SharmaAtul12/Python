
# Q1. Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
#  we are learning File I/O 
# using Java.
# I like programming in Java.

'''
with open("practice.txt","w") as f:
    f.write("Hi everyone\n we are learning File I/O \n using Java. \n I like programming in Java.")
'''

# Q2. WAF that replace all occurrences of “java” with “python” in above file.
'''
with open("practice.txt","r") as f:
    data = f.read()

new_Data = data.replace("Java", "Python")

with open("practice.txt","w") as f:
    f.write(new_Data)
'''

# Q3. Search if the word “learning” exists in the file or not.
'''
Method 1 => 
search_word = "lring"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(search_word) != -1): # Because find return index value . It Returns -1 if the substring is not found.
        print("Present")              # Otherwise It Returns The lowest index (position) of the substring if it is found in the given string.
    else:
        print("Not Present")
'''

'''
Method 2 => 
search_word = "lring"
with open("practice.txt","r") as f:
    data = f.read()
    if(search_word in data): 
        print("Present")              
    else:
        print("Not Present")
'''


# Q4. WAF to find in which line of the file does the word “learning” occur first.Print -1 if word not found.
'''
def check_for_line():
    word = "learning"
    data = True
    line_No = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline() #Agar data "" empty string hoga Us Case mm data ke value false ho jayegi. But agr Kuch bhi data h andar
            if(word in data):   # so data ke value true rhegi and loop chlega
                print("The Word Is Found In Line Number :",line_No)
                return
            line_No+=1
        return -1

print(check_for_line())
'''


# Q5. From a file containing numbers separated by comma, print the count of even numbers.
'''
count = 0
with open("number.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count+=1
    print(count)
'''
# "apple,banana,cherry" => data.split(",") => ["apple", "banana", "cherry"]
# Result: It returns a list of substrings that were separated by the comma. This list is then stored in the variable nums.


