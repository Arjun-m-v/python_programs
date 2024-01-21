# # Default constructor
# class Student:
#     def __init__(self):
#         print("Object Created")
#     name="Das"
#     roll_no=12
#     def fun(self):
#         print("Object Created")
# ob=Student()
# ob=Student()


# parameterised constructor
# class Student:
#     def __init__(self,name,rno,clss):
#         self.Name=name
#         self.Rollno=rno
#         self.Clss=clss
    
# ob=Student('Ajith',12,"BSc")
# print(ob.Name)
# cb=Student('Arjun',20,"BSc CS")
# print(cb.Name)

# class Student:
#     def __init__(self,name,rno,clss):
#         self.Name=name
#         self.Rollno=rno
#         self.Clss=clss
#     center="Calicut"
#     def display(self):
#         print(self.Name)


# ob=Student('Ajith',12,"BSc")
# # print(ob.Name)
# # print(ob.center)
# ob.display()



# cb=Student('Arjun',20,"BSc CS")
# # print(cb.Name)
# # print(cb.center)
# cb.display()



#-------------------------------------WORK-----------------------------------#
class Laptop:
    def __init__(self,brand,ram,rom):
        self.Brand=brand
        self.RAM=ram
        self.ROM=rom
    def ram(self):
        print(f"RAM of {self.Brand} is {self.RAM}")
    def rom(self):
        print(f"RAM of {self.Brand} is {self.ROM}")
# ob=Laptop()
ob=Laptop("hp",4,5)
ob.ram()
ob.rom()



#----------Destructor-----------#
