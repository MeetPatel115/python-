# write an input program to take name and write with that name 

name =input("Ener your name : ")

print("Good morning ", name)
print("gm"+" "+name)
print(f"Good Morning {name}")

# replace the value

letter="""
Dear <|Name|>,

you are  selected!!

<|date|>"""

print(letter)

print(letter.replace("<|Name|>",name).replace("<|date|>","15 jun 2026"))


# wirte a program to write the double space on the program 

print(letter.find("  "))

# replace double space with single

print(letter.replace("  ","2"))

# escape sequence method 

print("Dear Meet,\n this is a good start\n keep going \n which you best of luck \" Meet\" \n thank you")