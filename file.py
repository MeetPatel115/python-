with open("poem.txt") as f:
    data= f.readlines()
    for i in data :

        if "twinkle" in i:

            print("yes")
            print(i)

