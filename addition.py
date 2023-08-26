# class Member:
#     def __init__(self,fn):
#       self.fn=fn
  
#     def full_name(self):
#       return f"{self.fn}"
#     @staticmethod
#     def say_hello():
#        print("hello")
# n1=Member("salli")
# n2=Member("sara")
# n3=Member("ali")
# Member.say_hello()
# print(n1.full_name())

# class Skill:
#    def __int__(self):
#       self.skills=["html","hi"]
"""
kp
"""
# class A:
#    def __init__(self, c):
#        print("---------Inside class A----------")
#        self.c = c
#    print("Print inside A.")

#    def alpha(self):
#        c = self.c + 1
#        return c

# print(dir(A))
# print("Instantiating A..")
# a = A(1)
# print(a.alpha())
# class B:
#    def __init__(self, a):
#        print("---------Inside class B----------")
#        self.a = a

#    print(a.alpha())
#    d = 5
#    print(d)
#    print(a)

# print("Instantiating B..")
# b = B(a)
# print(a)

# from abc import ABC, abstractmethod
# class Bank(ABC):
#    def basicinfo(self):
#       print("This is a generic bank")
#       return "Generic bank: 0"
#    @abstractmethod
#    def withdraw(self):
#       pass
# class Swiss(Bank):
#    def __init__(self):
#       self.bal=1000
#    def basicinfo(self):
#       print("This is the Swiss Bank")
#       return "Swiss Bank: "+str(self.bal)
#    def withdraw(self,amount):
#       if amount <= self.bal:
#          self.bal -= amount 
#          print("Withdrawn amount: " + str(amount))
#          print("New balance: " + str(self.bal))
#          return self.bal
#       else:
#          print("Insufficient funds")
#          return self.bal
# def main():
#     assert issubclass(Bank, ABC), "Bank must derive from class ABC"
#     s = Swiss()
#     print(s.basicinfo())
#     s.withdraw(30)
#     s.withdraw(1000)

# if __name__ == "__main__":
#     main()

# import termcolor 
# import pyfiglet 


# print(dir(pyfiglet))
# print(pyfiglet.figlet_format(' sondos'))
# print(termcolor.colored(pyfiglet.figlet_format(' sondos'),color="yellow"))
# from datetime import datetime 
# print(datetime.datetime.now())
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().day)
# print(datetime.datetime.now().month)
# print("#"*40)

# print(datetime.datetime.min)
# print("#"*40)

# print(datetime.datetime.max)
# print("#"*40)

# print(datetime.datetime.now().time())
# print("#"*40)
# print(datetime.datetime.now().time().hour)
# print("#"*40)

# print(datetime.time.max)

# print("#"*40)
# print(datetime.datetime(1982,10,25))
# print(datetime.datetime(1982,10,25,10,45,55))
# print("#"*40)
# MyBirth=datetime.datetime(2004,1,15)
# print(MyBirth)
# print(MyBirth.strftime("%B"))
# print(MyBirth.strftime("%a"))
# print(MyBirth.strftime("%A"))
# print(MyBirth.strftime("%b"))
# print(MyBirth.strftime("%d /%B/ %Y"))





# file =open("sondos.txt")

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# from math import pi
# print(math.pi)
# names=["a","n","m"]
# names.insert(2,"Xi")
# print(names)
# for x in range(1,4):
#     print(int((str((float(x))))))
# s_d={1:"c",2:"t",3:"j"}
# for x in s_d:
#     print(x)
# def recursion(num):
#     print(num)
#     next = num - 3
#     if next > 1:
#         recursion(next)

# recursion(11)
# str = 'Pomodoro'
# for l in str:
#  if l == 'o':
#     str = str.split()
#     print(str, end=", ")
# def d():
#     color = "green"
#     def e():
#         nonlocal color
#         color = "yellow"
#     e()
#     print("Color: " + color)
#     color = "red"
# color = "blue"
# d()
# num = 9
# class Car:
#     num = 5
#     bathrooms = 2

# def cost_evaluation(num):
#     num = 10
#     return num

# class Bike():
#     num = 11

# cost_evaluation(num)
# car = Car()
# bike = Bike()
# car.num = 7
# Car.num = 2
# print(num)
class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass

d = D()
print(d.a())