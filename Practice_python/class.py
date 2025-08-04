# class Details:
#     x=10
#     def m1(self):
#         print('hello')
# d=Details()
# print(d.x)
# d.m1()

# name=input('enter the name')
# age=int(input('enter the age'))
# location=input('enter the location')
# class PersonalDetails:
#     def display_details(self,name,age,location):
#         print('name is',name)
#         print('age is',age)
#         print('location is',location)
# d=PersonalDetails()
# d.display_details(name,age,location)

# x=int(input('enter the number'))
# y=int(input('enter the number'))
# class MathOperations:
#     def sum(self,x,y):
#         print(f'the sum of {x} and {y} is {x+y}')
#     def difference(self,x,y):
#         print(f'the difference of {x} and {y} is {x-y}')
#     def product(self,x,y):
#         print(f'the product of {x} and {y} is {x*y}')
#     def quotient(self,x,y):
#         print(f'the quotient of {x} and {y} is {x/y}')
# m=MathOperations()
# m.sum(x,y)
# m.difference(x,y)
# m.product(x,y)
# m.quotient(x,y)

# z=30
# class A:
#     y=20         #class_variable
#     def m1(self):
#         x=10
#         print(x)
#         print(A.y)
# print(z)
# print(A.y)
# a=A()
# a.m1()

# name=input('enter name')
# age=int(input('enter age'))
# name1=input('enter name')
# exp=input('enter yr of experience')
# course=input('enter course')
# duration=input('enter duration')
# class Details:
#     def student_details(self,name,age):
#         print('name is',name)
#         print('enter is',age)
#     def staff_details(self,name1,exp):
#         print('enter name',name1)
#         print('enter yr of experience',exp)
# class Training:
#     def course(self,course):
#         print('course are ',course)
#     def duration(self,duration):
#         print('duration is',duration)
# d=Details()
# t=Training()
# d.student_details(name,age)
# d.staff_details(name1,exp)
# t.course(course)
# t.duration(duration)

# class info:
#     def __init__(self,id ,name,course):
#         print('id','=',id)
#         print('name','=',name)
#         print('course','=',course)
# i=info(1,'raj','JAVA')
# j=info(2,'varun','Python')
# k=info(3,'john','Python')

# class info:
#     def __init__(self,id ,name,course):
#         self.id=id
#         self.name=name
#         self.course=course
#     def m1(self):
#         print(self.id)
#         print(self.name)
#         print(self.course)
# i=info(1,'raj','JAVA')
# i.m1()
# j=info(2,'varun','Python')
# j.m1()
# k=info(3,'john','Python')
# k.m1()

# class mathsoperation:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def sum(self):
#             print('sum is',self.x+self.y)
#     def diff(self):
#             print('diff is',self.x-self.y)
#     def prod(self):
#             print('prod is',self.x*self.y)
#     def quot(self):
#             print('quot is',self.x/self.y)
# i=mathsoperation(10,20)
# i.sum()
# i.diff()
# i.prod()
# i.quot()

# class student:
#     def __init__(self,no,name,sub):
#         self.no=no
#         self.name=name
#         self.sub=sub
#     def display(self):
#         print('Number','=',self.no)
#         print('Name','=',self.name)
#         print('Subject','=',self.sub)
# i=student(1,'Sumanth','JAVA')
# i.display()

# class student:
#     def __init__(self,no,name,sub):
#         self.no=no
#         self.name=name
#         self.sub=sub
#     def display(self):
#         print('Number','=',self.no)
#         print('Name','=',self.name)
#         print('Subject','=',self.sub)
#         print('\n')
# i=student(1,'Sumanth','JAVA')
# i.display()
# j=student(2,'varun','Python')
# j.display()
# k=student(3,'john','Python')
# k.display()

# z=83
# class info:
#     y=48
#     print(z)
#     def m1(self):
#         self.y=80
#         print(self.y)
# i=info()
# i.m1()
# print(info.y)

# class TypesMethods:
#     def __init__(self):
#         print('init method')
#     def instance(self):
#         print('instance method')
#
#     @classmethod
#     def class_method(cls):
#         print('class method')
#
#     @staticmethod
#     def static_method():
#         print('static method')
#
# i=TypesMethods()
# i.class_method()
# i.static_method()
# i.static_method()

# class Assignment:
#     x=10
#     y=20
#     def m1(self,x):
#         self.z=30
#         print(Assignment.x)
#         print(Assignment.y)
#         print(self.z)
#         print(x)
#
#     @classmethod
#     def m2(cls,y):
#         print(y)
#         print(Assignment.x)
#         print(Assignment.y)
# i=Assignment()
# i.m1(50)
# i.m2(50)


# class student:
#     def __init__(self, name, rollno, m1,m2,m3):
#         self.name=name
#         self.rollno=rollno
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def calculate_average(self):
#         self.avg= (self.m1+self.m2+self.m3)//3
#         print(self.avg)
#
#     def display_grade(self):
#         if self.avg>90:
#             print('GRADE: A')
#         elif self.avg>=75 and self.avg<90:
#             print('GRADE: B')
#         elif self.avg>=50 and self.avg<75:
#             print('GRADE: C')
#         else:
#             print('GRADE: F')
#
# i=student('Shashwath',1,78,90,89)
# j=student('Pareekshith',2,89,78,69)
# k=student('Sumanth',3,78,90,67)
# i.calculate_average()
# j.calculate_average()
# k.calculate_average()
# i.display_grade()
# j.display_grade()
# k.display_grade()

class BankAccount:
    def __init__(self, name, account_no,balance):
        self.name=name
        self.account_no=account_no
        self.balance=balance
    def deposit(self,add):
        self.balance=self.balance+add
        print('Amount deposited:',add)
    def withdraw(self, deduct):
        if self.balance>=deduct:
            self.balance=self.balance-deduct
            print('Amount withdrawn:',deduct)
        else:
            print('Insufficient balance')

    def display(self):
        print('Account holder:', self.name)
        print('Account number:', self.account_no)
        print('Current balance:', self.balance)

i=BankAccount('Shashwath',123456789,15000)
i.deposit(20000)
i.withdraw(16000)
i.display()






