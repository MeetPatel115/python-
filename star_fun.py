def star(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        print("")
star(3)

## convert it into inch to cm

def in_cm(me):

    return me*2.54

mes=int(input("Enter the value that has to convert : "))

print(f"The {mes} of ince = {in_cm(mes)} cm ")


## print the multiplication table with function
def table(mul):
    for i in range(11):
        print(f" {mul} x {i} = {mul*i}")

mul=int(input("Enter the table name :"))
table(mul)

## Emeove the give word from list

def rm(l,word):
    temp=[]
    for i in l:
        if i!=word:
            temp.append(i.strip(word))
    return temp

l=['Rohan', "Meet","an"]

print(rm(l,"an"))