#Write a Python program that prints the string s without the characters located at even indices.
#If the string is empty or only has one character, print it intact.

text = input("Enter the string:- ")
print(text[1::2])
new_text=""

#2nd method
'''
for i in range(len(text)):
    if i%2!=0:
        new_text+=text[i]
print(new_text)    
'''
