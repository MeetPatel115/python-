def table(n):
    file=""
    for i in  range(1,11):
        file+=f" {n} x {i} = {n*i}\n"
    
    with open(f'Tables/table_{n}',"w") as f:
        f.write(file)


for i in  range(2,21):
    table(i)