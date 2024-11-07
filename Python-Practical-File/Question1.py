# 1. Write a program to perform various arithmetic operations with 2 objects of class complex.

class Complex:
    def __init__(self):
        self.a=int(input("Enter First number : "))
        self.b=int(input("Enter Second number : "))
    def addtion(self):
        return self.a+self.b
    def substraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        return self.a/self.b
    def difference(self):
        if(self.a>self.b):
            return self.a-self.b
        else:
            return self.b-self.a

o1=Complex()
print("Addition is :",o1.addtion())
print("Substraction is :",o1.substraction())
print("Multiplication is :",o1.multiplication())
print("Division is :",o1.division())
print("Difference is :",o1.difference())