#----------Global variable
a="apple"
def funct():
    print(a)
funct()
if True:
    print(a)
print(a)


#----------Local variable
def funct():
    a="apple"
    print(a)
funct()
if True:
    print(a)
print(a)


#----------Local varibale to global variable
def funct():
    global a
    a="apple"
    print(a)
funct()
if True:
    print(a)
print(a)