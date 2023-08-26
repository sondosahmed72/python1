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




# import os
# print(os.getcwd())
# print(os.path.dirname(os.path.abspath(__file__)))
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print(os.getcwd())

# print(os.path.abspath(__file__))

# #file =open("sondos.txt")


#myfile = open(r"C:\Users\sondo\OneDrive\Desktop\python\sondos.txt", "a")
# print("#"*40)
# print(myfile)
# print("#"*40)
# print(myfile.name)
# print("#"*40)
# print(myfile.mode)
# print("#"*40)
# print(myfile.encoding)

# print(myfile.read())
# print(myfile.read(5))

# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline(5))

# print(myfile.readlines())
# print(type(myfile.readlines()))

# for line in myfile:
#     print(line)
#     if line.startswith("07"):
#       break
 
# myfile.close()

# myfile.write("sandosaaaaaaaaaaaaaaaa\n" *100)
# myList =["sondos ","ahmed ","haba"]
# myfile.writelines(myList)

# myfile.truncate(5)
# print(myfile.tell())
# myfile.seek(6)
# print(myfile.read())

# ''' 
# Import statements: 
#     1. Import the built-in json python package
#     2. From employee.py, import the details function and the employee_name, age, title variables
# '''
# import json
# from employee import details , employee_name , age ,title

# def create_dict(name, age, title):
#     """ Creates a dictionary that stores an employee's information

#     [IMPLEMENT ME]
#         1. Return a dictionary that maps "first_name" to name, "age" to age, and "title" to title

#     Args:
#         name: Name of employee
#         age: Age of employee
#         title: Title of employee

#     Returns:
#         dict - A dictionary that maps "first_name", "age", and "title" to the
#                name, age, and title arguments, respectively. Make sure that 
#                the values are typecasted correctly (name - string, age - int, 
#                title - string)
#     """
#     ### WRITE SOLUTION HERE
#     emp_dis ={
#        "first_name": str(employee_name),
#         "age": int(age),
#         "title": str(title)
#     }
#     return emp_dis
#     raise NotImplementedError()


# employee_dict = create_dict()
# json_object = json.dumps(employee_dict)
# def write_json_to_file(json_obj, output_file):
#     """ Write json string to file

#     [IMPLEMENT ME]
#         1. Open a new file defined by output_file
#         2. Write json_obj to the new file

#     Args:
#         json_obj: json string containing employee information
#         output_file: the file the json is being written to
#     """
#     ### WRITE SOLUTION HERE
#     new_file = open(output_file,"w")
#     newfile.write(json_object)
#     newfile.close()
#     raise NotImplementedError()

# def main():
#     # Print the contents of details() -- This should print the details of an employee
#     details()

#     # Create employee dictionary
#     employee_dict = create_dict(employee_name, age, title)
#     print("employee_dict: " + str(employee_dict))

#     ''' 
#     Use a function called dumps from the json module to convert employee_dict
#     into a json string and store it in a variable called json_object.
#     '''
#     ### WRITE YOUR CODE BY MODIFYING THE LINE BELOW
#     # In the line below replace the None keyword with your code. 
#     # The format should look like: variable = json.dumps(dict)
#     json_object = None
#     print("json_object: " + str(json_object))

#     # Write out the json object to file
#     write_json_to_file(json_object, "employee.json")

# if __name__ == "__main__":
#     main()



# import numpy as np
# print(np.__version__)

# my_list=[1,2,3,4,5]
# my_array=np.array([1,2,3,4,5]) 
# print(my_list)
# print(my_array)
# print("#"*50)
# print(my_array[0])
# print(my_list[0])
# print("#"*50)
# a=np.array(10)
# b=np.array([10,20])
# c=np.array([[10,20],[10,0]])
# d=np.array([[[10,500],[20,88]],[[10,100],[0,5]]])
# print(a)
# print("#"*50)

# print(b)
# print("#"*50)

# print(c)
# print("#"*50)

# print(d)
# print("#"*50)
# print(d[1,1,1])
# print(d[1,1,-1])
# print("#"*50)
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)
# print("#"*50)
# my_custoum_array=np.array([1,2,3],ndmin=3)
# print(my_custoum_array)
# print(my_custoum_array[0,0,0])



# import time
# import sys
# elements =150000000000000000000
# my_list1=range(elements)
# my_list2=range(elements)

# my_array1=np.arange(elements)
# my_array2=np.arange(elements)
# list_start=time.time()
# list_res=[(n1+n2) for n1,n2 in zip(my_list1,my_list2)]
# print(f"list time : {time.time()-list_res}")
# for n1,n2 in zip(my_list1,my_list2):
#     print(n1+n2)
# array_start=time.time()
# array_res=my_array1+my_array2
# print(f"array time :{time.time()-array_res}")
# import sys
# my_array =np.arange(100)
# print(my_array)
# print(my_array.itemsize)
# print(my_array.size)
# print(f"All Bytes: {my_array.itemsize*my_array.size}")
# print("#"*50)
# my_list=range(100)
# print(sys.getsizeof(my_list[0]))
# print(len(my_list))
# print(f"All Bytes: {sys.getsizeof(1)*len(my_list)}")


# a=np.array(["A","B","c"])
# print(a[2:3])

# b=np.array([["A","B","X"],["C","D","Y"],["E","F","Z"],["M","N","O"]])
# print(b.ndim)
# print(b[:3])
# print("#"*50)
# print(b[:3,:2])
# print("#"*50)
# print(b[2:,0:3])

# my_array1=np.array(["A","B","c"])
# my_array2=np.array([1,2,3,4,5]) 
# my_array3=np.array([1.5,2.9,3.9]) 
# print(my_array1.dtype)
# print(my_array2.dtype)
# print(my_array3.dtype)
# print("#"*50)

# my_array1=np.array(["A","B","c"])
# my_array2=np.array([1,2,3,4,5],dtype=float) 
# my_array3=np.array([1.5,2.9,3.9],dtype=int)

 
# my_array2=np.array([1,2,3,4,5]) 
# print(my_array2.dtype)
# print(my_array2)
# print("#"*50)
# my_array2=my_array2.astype("float")
# print(my_array2.dtype)
# print(my_array2)


# my_array2=np.array([1,2,3,0,5]) 
# print(my_array2.dtype)
# print(my_array2)
# print("#"*50)
# my_array2=my_array2.astype("bool")
# print(my_array2.dtype)
# print(my_array2)

# my_array2=np.array([1,2,3,0,5],dtype="f") 
# print(my_array2.dtype)
# print(my_array2[0].itemsize)
# my_array2=my_array2.astype("float")
# print(my_array2.dtype)
# print(my_array2[0].itemsize)

# my_array2=np.array([1,2,3,0,5]) 
# print(my_array2.shape)


# d=np.array([[[10,500],[20,88]],[[10,100],[0,5]]])
# print(d.shape)
# print(d.ndim)

# my_array2=np.array([1,2,3,0,5,8]) 
# reshaped=my_array2.reshape(2,3)

# print(reshaped.shape)
# print(reshaped.ndim)

# a=np.zeros(10)
# print(a)
# b = np.full((2,10), 0.7)
# print(b)
# c = np.linspace(0,25,8)
# print(c)
# import pandas as pd
# students=({'std_id': [1001,1002,1003,1004,1005],
#            "std_name":["ahmed","ali","mohamed","salli","mai"],
#            "marks":[480,570,470,510,490]})
# df=pd.DataFrame(students)
# print(df)
# print(df.describe)
# student_name=["ahmed","ali","mohamed","salli","mai"]
# marks=[1001,1002,1003,1004,1005]
# x=pd.Series(data=marks,index=student_name)
# print(x)


# b = pd.DataFrame({
#     "Letters" : ['a', 'b', 'c', 'd', 'e', 'f'],
#     "Numbers" : [12, 7, 9, 3, 5, 1]  })

# print(b.sort_values(by="Numbers"))
# b = b.assign(new_values = b['Numbers']*3)
# print(b)

# import nltk
# # nltk.download('punkt')

# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# print(word_tokenize(text))
# # Print statement 2
# print(nltk.tokenize.sent_tokenize(text))
# text1="Bonjour M. Adam,commenr allez-vous?"
# print(nltk.tokenize.sent_tokenize(text,"frensh"))



# stopwords = stopwords.words("english")
# new_text = []
# for i in text.split():
#     if i not in stopwords:
#         new_text.append(i)

# # Print statement 3
# print(new_text)
def add(a,b):
    return a+b