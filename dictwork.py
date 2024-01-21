wrd="hi hello hei hello red hello red hi hi"
a=wrd.split(" ")
print(a)
res={}
for i in a:
    if i in res:
        res[i]+=1
    else:
        res[i]=1
print(res)