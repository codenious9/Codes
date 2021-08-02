text = input("Enter the string:- ")
number_str= 3
if len(text)<6:
    print("overlapped charactors")
else:
    new_text= text[:3]+text[len(text)-number_str:]
    print(new_text)
