def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    elif c>a and c>b:
        return c
    else:
        return "Equal"


a=int(input("Enter a "))
b=int(input("Enter b "))
c=int(input("Enter c "))

ans=greatest(a,b,c)
print(f"The Gratest number is {ans}")