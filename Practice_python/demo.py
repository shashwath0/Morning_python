# r=range(5,55,5)
# li=list(r)
# print(li)

# r=range(50,4,-5)
# li=list(r)
# print(li)

# r=range(1,100,2)
# li=list(r)
# print(li)

# r=range(99,0,-2)
# li=list(r)
# print(li)

# r=range(2,101,2)
# li=list(r)
# print(li)

# r=range(100,0,-2)
# li=list(r)
# print(li)

# r=range(49,-24,-8)
# li=list(r)
# print(li)

# r=range(24,-1,-4)
# li=list(r)
# print(li)

# r=range(41,-10,-7)
# li=list(r)
# print(li)

# r=range(5,42,7)
# li=list(r)
# print(li)

# di={'Name':'Shashwath K Rao',
#             'Age':23,
#             'Location':'Bangalore'
# }
# di['Ph.no']=854083
# print(di)
# di['Location']='Mangalore'
# print(di)

# edict={'eno':84774,'ename':'Shashwath','esal':60000}
# edict['esal']=50000
# print(edict)
# edict['elocation']='church street'
# print(edict)

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

# def fun(x,y):
#     return f'sum of{x} and {y} is {x+y}',f'product of{x} and {y} is {x*y}',f'divison of{x} and {y} is {x/y}',f'substraction of{x} and {y} is {x-y}',f'remainder of{x} and {y} is {x%y}'
# x=int(input('enter the first digit'))
# y=int(input('enter the second digit'))
# t=fun(x,y)
# print(t)

# x=int(input('enter the first digit'))
# y=int(input('enter the second digit'))
# if x>y:
#     print('x is bigger number' )
# else:
#     print('y is bigger number')

# x=int(input('enter the number'))
# if x%2==0:
#     print('the number is even')
# else:
#     print('the number is odd')

# x=int(input('enter the first digit'))
# y=int(input('enter the second digit'))
# z=int(input('enter the third digit'))
# if x>y and x>z:
#     print('x is bigger number' )
# elif y>z:
#     print('y is bigger number')
# else:
#     print('z is bigger number')

# x=input('enter the character')
# if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
#     print('vowel')
# else:
#     print('conconant')


# x=int(input('enter a year'))
# if (x%400==x) or (x%4==0 and x%100!=0):
#     print(x,'is a leap year')
# else:
#     print(x,'is not a leap year')

# x=input('enter a string')
# y=x[::-1]
# if x==y:
#     print(x,'is a pallindrome')
# else:
#     print(x,'is not a pallindrome')

# x=int(input('enter the length'))
# y=int(input('enter the bredth'))
# if x==y:
#     print('the given figure is a square')
# else:
#     print('the given figure is a rectangle')

# x=input('enter the gender')
# y=int(input('enter the height'))
# if ((x=='male'or x=='Male'or x=='m'or x=='M') and y>=188)or((x=='female'or x=='Female'or x=='f'or x=='F') and y>=175):
#     print('the given candidate is eligible for admiddion')
# else:
#     print('the given candidate is not eligible for admission')

# x=2
# while x<=100:
#     print(x,end=' ')
#     x=x+2
#
# x=1
# while x<=99:
#     print(x,end=' ')
#     x=x+2

# x=2
# while x<=65536:
#     print(x,end=' ')
#     x=x**2

# x=3125
# while x>=5:
#     print(x,end=' ')
#     x=x/5

# x=1
# while x<=10:
#     print(f'1*{x}={1*x}',end=' ')
#     x=x+1
#     print('\r')
# x=2
# while x<=20:
#     print(x,end=' ')
#     x=x+2
# print('\r')
# x=3
# while x<=30:
#     print(x,end=' ')
#     x=x+3
# print('\r')
# x=4
# while x<=40:
#     print(x,end=' ')
#     x=x+4
# print('\r')
# x=5
# while x<=50:
#     print(x,end=' ')
#     x=x+5
# print('\r')
# x=6
# while x<=60:
#     print(x,end=' ')
#     x=x+6
# print('\r')
# x=7
# while x<=70:
#     print(x,end=' ')
#     x=x+7
# print('\r')
# x=8
# while x<=80:
#     print(x,end=' ')
#     x=x+8
# print('\r')
# x=9
# while x<=90:
#     print(x,end=' ')
#     x=x+9
# print('\r')
# x=10
# while x<=100:
#     print(x,end=' ')
#     x=x+10
# print('\r')

# li=[10,20,30,40,50]
# for i in range (len(li)-1,-1,-2):
#     print(li[i],end=' ')
# print('\n')
# for i in range (len(li)-2,-1,-2):
#     print(li[i],end=' ')

# li=[10,20,13,61,50]
# for i in range (len(li)-1,-1,-2):
#     print(li[i],end=' ')
# print('\n')
# for i in range (len(li)-2,-1,-2):
#     print(li[i],end=' ')
# print('\n')
# for i in li:
#     if i%2==0:
#         print(i,'is even element')
#     else:
#         print(i,'is odd element')
#
# sum=0
# for i in li:
#     sum=sum+i
# print(sum,'is sum of all elements')
# li=[10,20,13,61,50]
# even_sum=0
# odd_sum=0
# for i in li:
#     if i%2==0:
#         even_sum=even_sum+i
#     else:
#         odd_sum=odd_sum+i
# print(even_sum,'is sum of even elements')
# print(odd_sum,'is the sum of odd elements')
#
# li=[10,20,13,61,50]
# print('sum of elements at odd and even indices')
# even_sum=0
# odd_sum=0
# for i in range(0,len(li),2):
#         even_sum=even_sum+li[i]
# for i in range(1, len(li), 2):
#         odd_sum=odd_sum+li[i]
# print(even_sum,'is sum of even indices')
# print(odd_sum,'is the sum of odd indices')

# take a string as input from keyboard.calculate the number of words and spaces:

# li=input('enter the string: ')
# space=0
# words=1
# for i in li:
#   if i==' ':
#     space=space+1
#     words =words+1
# print(space,'is no of space ')
#
# print(words,'is no of words ')


# st = input('enter the string:')
# words = 0
# space = 0
# for i in range(len(st)):
#     if st[i] == ' ':
#         space = space + 1
#     elif i == 0 or st[i - 1] == ' ':
#         words = words + 1
#
# print('the number of spaces in input string', space)
# print('the the number of words in input string', words)

# take a list of vowels .input a character from keyboard .check whether the input character is vowel or not'''

# vowel_list=['a','e','i','o','u']
# x=input('enter the character')
# for i in vowel_list:
#     if x==i:
#       print('vowel')
#       break
# else:
#     print('conconant')

# li=[40,10,30,1,15]
# biggest=0
# for i in li:
#     if i>biggest:
#         biggest=i
# print(biggest)
# li=[40,10,30,1,15]
# smallest=40
# for i in li:
#     if i<smallest:
#          smallest=i
# print(smallest)

# di={
#     'x':10,
#     'y':20
#     }
# for i,j in di.items():
#         print(i,'=',j)

# di={
#     'w':input('enter the house number: '),
#     'x':input('enter the street: '),
#     'y':input('enter the city: '),
#     'z':input('enter the pincode: ')
# }
# for i, j in di.items():
#     print(i,'=',j)

# li=[]
# for i in range(5):
#     num=int(input('enter the number'))
#     li.append(num)
#     print(li)

num=int(input('enter the number: '))
res=num
rev=0
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
if rev==res:
    print(res,'is a pallendrome number')
else:
    print(res,'is not a pallendrome122 number')