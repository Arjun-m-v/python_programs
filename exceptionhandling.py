# --- --- try , except , finally --- ---
try:
    a=int(input("Enter a number="))
    b=int(input("Enter another number="))
    c=a/b
    print(c)
except:
    print("Error occured!!")
finally:
    print("Program ended!!")


# --- --- Using else --- ---
try:
    a=int(input("Enter a number="))
    b=int(input("Enter another number="))
    c=a/b
    print(c)
except:
    print("Error occured!!")
else:                                                # Used to perform if no exceptions are found
    print("No exceptions!!")
finally:
    print("Program ended!!")


# --- --- Value error and Zero Division Error --- ---
try:
    a=int(input("Enter a number="))
    b=int(input("Enter another number="))
    c=a/b
    print(c)
except ValueError:
    print("Value Error occured!!")
except ZeroDivisionError:
    print("Error because of division by Zero")
else:                                                
    print("No exceptions!!")
finally:
    print("Program ended!!")


# --- --- Default error message by error class --- ---
try:
    a=int(input("Enter a number="))
    b=int(input("Enter another number="))
    c=a/b
    print(c)
except ValueError as msg:
    print(msg)
except ZeroDivisionError as msg:
    print(msg)
else:                                                
    print("No exceptions!!")
finally:
    print("Program ended!!")


# --- --- Userdefined Exceptions --- ---
a=int(input("Enter a number="))
b=int(input("Enter another number="))
if a>b:
    print(a-b)
else:
    raise Exception("a is less than b")


# --- --- Custom error messages in Userdefined Exceptions --- ---
class LessThanError(Exception):
    pass
a=int(input("Enter a number="))
b=int(input("Enter another number="))
if a>b:
    print(a-b)
else:
    raise LessThanError("a is less than b")