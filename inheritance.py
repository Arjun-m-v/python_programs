# #---------------------Simple inheritance-------------------------
# class A:
#     ram="Ram is 4GB"
#     def fun(self):
#         print("Boom")

# class B(A):
#     pass

# b=B()
# print(b.ram)
# b.fun()


# #           Super class              #
# class A:
#     ram="Ram is 4GB"
#     def fun(self):
#         print("Boom")

# class B(A):
#     def display(self):
#         print(super().ram)

# b=B()
# # print(b.ram)
# # b.fun()
# b.display()


#----------------------------------Types of inheritance-----------------------------------#

# Single inheritance----

# class A:
#     ram="Ram is 4GB"
#     def fun(self):
#         print("Boom")

# class B(A):
#     pass

# b=B()
# print(b.ram)
# b.fun()


# Multiple inheritance----
# class A:
#     ram="Ram is 4GB"
    

# class B:
#     def fun(self):
#         print("Boom")

# class C(A,B):
#     pass

# c=C()
# print(c.ram)
# c.fun()

# MUltilevel inheritance----------
# class A:
#     ram="Ram is 4GB"

# class B(A):
#      def fun(self):
#         print("Boom")

# class C(B):
#     pass

# c=C()
# print(c.ram)
# c.fun()


# Hierarchical inheritance----------
# class A:
#     ram="Ram is 4GB"
#     name="name is arjun"
#     def fun(self):
#         print("Boom")

# class B(A):
#      pass

# class C(A):
#     pass

# class D(A):
#     pass

# a=A()
# b=B()
# c=C()
# print(a.ram)
# print(b.name)
# c.fun()



# # Hybrid inheritance---------
# class A:
#     ram="Ram is 4GB"
#     name="name is arjun"
#     def fun(self):
#         print("Boom")

# class B(A):
#      pass

# class C(A):
#     pass   

# class D(B,C):
#     pass

# d=D()
# print(d.ram)
# print(d.name)
# d.fun()  


