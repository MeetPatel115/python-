words=["twinkle","star","world"]


with open("poem.txt") as f:
    content=f.read()
for word in words:
    content=content.replace(word, "#"*len(word))
print(content)
with open("poem.txt",'w') as f:
    f.write(content)