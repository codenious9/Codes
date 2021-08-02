def reversed(text):
    reversed_string=""
    for i in text:
        reversed_string=i+reversed_string # the order in which i concatenates with reversed_string matters. 
    print("The reversed string is ",reversed_string)

text = input("Enter the string:- ")
reversed(text)
