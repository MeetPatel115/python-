#  create a dict with hindi word with english translation



# dict1={"madaad":"Help",
#        "kurshi":"chair",
#        "darwaza":"door"}
# word=input("Enter the word for meaning :")
# print(dict1[word])


# enter 8 numbers from user and writ the uiqe number of that word


# l1=[]

# w=int(input("Enter number of words in the dict :"))

# for i in range(w):
#     temp=int(input("Enter number :"))

#     l1.append(temp)

# print(set(l1))

# can we add set as 18 and "18" as string


s={19,1,24,2,"19",35}
print(s)

s1=set()

s1.add(2)
s1.add(2.0)
s1.add("2")

print(len(s1),s1)

#  enter 5 firnde as their key and favourite subject as value


# names=["meet","vraj","parth","jenish"]

# di={}

# for i in range(4):
#     sub=input(f"Enetr your favourite subject {names[i]}")
#     di[names[i]]=sub
# print(di)


#can we change the value in set 

s={1,3,2,5,3,23}
print(s)
s.update({33,21})

print(s)