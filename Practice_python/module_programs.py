# import calendar
# year=int(input('enter the year: '))
# month=int(input('enter the month: '))
# display=calendar.month(year,month)
# print(display)

# import datetime
# print(datetime.datetime.now())
#
# import math
# print(math.factorial(5))

# num=int(input('enter the number'))
# fact=num
# for i in range(1,num):
#     fact*=i
# print('Factorial of ',num,'is',fact)

# b=int(input('Enter the bredth: '))
# h=int(input('Enter the height: '))
# tri=1/2*b*h
# print(tri)

# miles=int(input('Enter miles: '))
# km=1.6*miles
# print(km)

# cel=int(input('enter the celcius: '))
# far=(cel*9/5)+32
# print(far)

# num=int(input('Enter the number'))
# if num==0:
#     print('number is zero')
# elif num<0:
#     print('number is negative')
# else:
#     print('number is positive')

x=int(input('Enter the number'))
i=1
while x<=100 and i<10:
    i=i+1
    print(f'{i}*{x}={i * x}')