a=[1,2,1,1,2,3,2,1,3,4,56,4,3,2,1,56]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
