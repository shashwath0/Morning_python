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

x=input('enter the gender')
y=int(input('enter the height'))
if ((x=='male'or x=='Male'or x=='m'or x=='M') and y>=188)or((x=='female'or x=='Female'or x=='f'or x=='F') and y>=175):
    print('the given candidate is eligible for admiddion')
else:
    print('the given candidate is not eligible for admission')