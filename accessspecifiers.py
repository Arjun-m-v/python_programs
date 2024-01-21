# Public = Default
# Protected = uses _ as prefix for the memebr (conecptual method)
# Private = uses __ as prefix for the member


class Main:
    __name="Main"
    def main_meth(self):
        print(self.__name)


ob=Main()
# print(self.__name)
ob.main_meth()

# class Sub(Main):
#     def fun(self):
#         print(super().__name)
#         super().main_meth()

# os=Sub()
# print(os.__name)
# os.main_meth()
        