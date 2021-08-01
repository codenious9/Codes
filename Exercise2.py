text = input("Enter the string:- ")
index = int(input("Enter the index:- "))
if not text:
    print("Empty String")
elif index>len(text):
    print("Index out of range") 
else:
    print(text[index])
