def cel_far(cel):
    return (cel*9/5)+32
def far_cel(far):
    return (far-32)*5/9


temp = int(input("Enter the Teamprature : "))

choice=input("want to convert celcius to far then go with 'C' other wise 'F'")
if choice=='C':
    ans=cel_far(temp)
    print(f"The farhinte is  {ans}")
else:
    ans=far_cel(temp)
    print(f"The Celcius is {ans}")

