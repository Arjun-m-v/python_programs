#---------- arbritiry args
#---------- arbritiry args
def find(a,*b):
    print(a)
    print(b)

find(10,20,30,40)

#----------keyword args
def find(a,b):
    print(a)
    print(b)

find(a=10,b=20)

#----------arbrotory keyword args
def find(a,**b):
    print(a)
    print(b)

find(a=10,b=20,c=30)

#----------default args

def find(a,b=5):
    print(a)
    print(b)

find(10)