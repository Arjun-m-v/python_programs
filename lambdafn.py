# def sum(a,b):
#     c=a+b
#     return c
# res=sum(10,20)
# print(res)

# x=lambda a,b:a+b
# print(x(10,20))

# --- --- --- Applications of lambda function --- --- ---
# # --- --- --- Filter --- --- ---
# a=[2,34,5,11,99]
# b=list(filter(lambda a:a>10,a))
# print(b)

# # --- --- --- Map --- --- ---
# a=[2,3,5,1,9]
# b=list(map(lambda a:a*10,a))
# print(b)

# --- --- --- Reduce --- --- ---
# c=[1,2,3,4,5]
# b=list(reduce(lambda a,b:a+b))
# print(b)


# a=[1,2,34,3,67,4]
# def sq(num):
#     return num**2
# # b=[]
# # for i in a:
# #     b.append(sq(i))
# # print(b)
# b=list(map(sq,a))
# print(b)

# # --- --- --- Map --- --- ---
# a=[1,2,34,3,67,4]
# b=list(map(lambda num:num**2,a))
# print(b)

# # --- --- --- Filter --- --- ---
# a=[1,2,34,3,67,4]
# b=list(filter(lambda num:sum,a))
# print(b)

from functools import reduce
a=[1,2,34,3,67,4]
res=reduce(lambda tot,num:tot+num,a)
print(res)