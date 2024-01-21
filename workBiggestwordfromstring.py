a=input("Enter a string=")
l=0
res=""
b=a.split()
for i in b:
    if l<len(i):
        l=len(i)
        res=i
print(res)
   