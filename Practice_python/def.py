# def details(x,y):
#     print(x,y)
# details('Shashwath','Bangalore')

# def arith(x,y):
#     print(x+y)
# x=int(input('enter the first digit'))
# y=int(input('enter the second digit'))
#
# arith(x,y)

# def fun(x):
#     print(x[::-1])
# x=input('enter the string')
# fun(x)

# def details(name, location):
#     return f'{name}, {location}'
# res=details('Shashwath','Banglore')
# print(res)

# def arith(x,y):
#     return f'sum of{x} and {y} is {x+y}'
# x=int(input('enter the first digit'))
# y=int(input('enter the second digit'))
# sum=arith(x,y)
# print(sum)

# def fun(x):
#     return x[::-1]
# x=input('enter the string')
# string=fun(x)
# print(string)

def fun(x,y):
    return f'sum of{x} and {y} is {x+y}',f'product of{x} and {y} is {x*y}',f'divison of{x} and {y} is {x/y}',f'substraction of{x} and {y} is {x-y}',f'remainder of{x} and {y} is {x%y}'
x=int(input('enter the first digit'))
y=int(input('enter the second digit'))
t=fun(x,y)
print(t)