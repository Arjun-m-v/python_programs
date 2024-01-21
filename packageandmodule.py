from pack1.exmodule1 import fact,add

from pack1 import name

from pack1.subpack.subsubpack.exmodulesspack import fun

a=int(input("Enter first number="))
b=int(input("Enter seconf number="))


rest1=fact(a)
print(rest1)
rest2=fact(b)
print(rest2)

print(add(rest1,rest2))

print(name)

fun()