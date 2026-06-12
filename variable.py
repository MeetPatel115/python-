# write a python to add 2 numberes

import statistics
c=input("Enter the variable for just checking: ")
a=int(input("enter first value: "))
b=int(input("enter second value: "))

print("Addition of both the nubers: ",a+b)

# find the number of reminder if we divide it with a/b


# we use module function to find the reminder


print("Remiber if we divide a with b: ",a%b)

# check the type of variable for the given charcter


print(type(c))
print(type(a))


# check the a is grater that b of not

print("Is a grater than b or not: ",a>b)
if a>b: 
    print(" A is grater")
else: 
    print("A is smaller than B")

# find the average of a and b


print("Average of a and b ", (a+b)/2)
print("printing average using the mean function in sta: ", statistics.mean([a,b]))

#find the suare of the number c 


print("sqaure of a is ",a*a,a**2)
