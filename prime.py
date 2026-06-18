n= int(input("Enter a number"))
a=True
for i in range(2,n):
    if n%i==0:
        a=False

if a:
    print(f" This is {n } Prime Number")
else:
    print(f"This is {n} not a Prime Number")