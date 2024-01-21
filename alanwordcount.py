f=open("alan.txt")
a=str(f.readlines())
b=a.split(" ")
#print(b)
res=0
for i in b:
    res+=1
    print(res)