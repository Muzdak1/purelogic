para = "This is a name"
print(len(para))
# strings are case sensitive
print(para[0])
# It returns first char from the end of string
print(para[-1])

#  String slicing

print(para[0:3])
print(para[:3])

#----

print(para[0:])
print(para[:])

print(para[0:-1])
b = []

word_list = para.split()
print(word_list)

# print(a)
"""---- all the slicing will have a new memory location as string is immutable class the orignal value of
 para will remain the same """
 # String Formating

first_name = "Ali"
last_name = "M"
full = f"{first_name} {last_name} {2+2}"
# we can add any expression between these {bracket}
print(full)

# Methods of String
para = "This is a name"
print(para.upper())
print(para.lower())
print(para.title()) # convert it to TitleCase
print(para.strip())
print(para.lstrip())
print(para.rstrip())
# remove extra white spaces
print(para.find("name"))
# Find the index of character
# print(para.replace("name", "Name"))
print("is" in para)
#  to find out the word in string



