a=157
temp=a
res=0
while a>0:
    rem=a%10
    res=res+(res**3)
    a=a//10
if temp==res:
    print("Armstrong number")
else:
    print("Not armstrong number")