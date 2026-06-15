# print the sum of n number 

def sum_n(num):
    if num<=0:
        return 0
    if num==1:
        return 1
    return num+sum_n(num-1)

print("The total sum of first n number is ",sum_n(-5))