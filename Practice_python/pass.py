# def fun(*args):
#     for i in args:
#         print(i,end=' ')
# fun(1,2,3,4,5)

# def fun(x,*y,z=100):
#     print(x)
#     print(y)
#     print(z)
# fun(10,20,30,40,60)
# fun(10,20,30,40)
# fun(10,20,30,z=100)

# def fun(x,*y,z):
#     print(x)
#     print(y)
#     print(z)
# fun(1,2,5,5,7,z=6)

# def fun(x,y,*z):
#     print(x)
#     print(y)
#     print(z)
# fun(1,2,5,5,7,6)

# def fun(name,blood_group,*disease_suffering,email='not given'):
#     print(name)
#     print(blood_group)
#     for i in disease_suffering:
#         print(i,end=' ')
#     print('\n')
#     print(email)
# fun('Sumanth','A+','cold','caugh','fevre',email='sumanth22@gmail.com')

# def fun(Student_name,*email,**house_address):
#     print(Student_name)
#     for i in email:
#         print(i,end=' ')
#         print('\n')
#     for i,j in house_address.items():
#         print(f"{i}={j}")
# fun('Sumanth','sumanth8022@gmail.com','sum4899@gmail.com',house_address=48748)

# li=[]
# li.append((1,2))
# print(li)

# li=[]
# for i in range(10):
#     num=int(input('enter the number'))
#     li.append(num)
# print(li)
# pos=int(input('enter the position '))
# obj=int(input('enter the object'))
# li.insert(pos,obj)
# print(li)

# li=[3,5,7,0,2,9]
# ele=int(input('enter the element to delete from list'))
# if ele in li:
#    li.remove(ele)
#    print(li)
# else:
#     print('element is not avaliable')

# # li=[2,4,6,7,8,9]
# pos=int(input('enter the position to delete from list'))
# if pos in range(len(li)):
#    li.pop(pos)
#    print(li)
# else:
#     print('position is not avaliable')

# li=[8,7,9,5,6,4]
# ele=int(input('enter the element to search its position'))
# if ele in li:
#    print(li.index(ele))
# else:
#     print('-1')

# tu=(1,2,3,4,5)
# ele=int(input('enter the element whose index has to be determined '))
# if ele in tu:
#     print('the index of',ele,'is',tu.index(ele))
# else:
#     print(ele,'is not present in the tuple')

# se=set()
# for i in range(5):
#     num=int(input('enter the number'))
#     se.add(num)
# print(se)

# s={2,4,5,678,9,9}
# ele=int(input('enter the element to be deleted '))
# if ele in s:
#     print(s)
# else:
#     print(ele,'is not present in set')

# dict={}
# dict['name']=input('enter the name')
# dict['email']=input('enter email')
# dict['mobile']=int(input('enter mobile no.'))
# dict['city']=input('enter city')
# dict['pin']=input('enter pincode')
# print(dict)
# for i,j in dict.items():
#         print(f"{i}={j}")
# dict['name']='chalan'
# for i,j in dict.items():
#         print(f"{i}={j}")
# print(dict)

di={'name':'Shashwath','email':'fhghdhd@gmail.com','mobile':'9876545678'}
# key=input('enter the key to be checked: ')
# if key in di.keys():
#     di.pop(key)
# print(di)

# value=input('enter the value to be checked')
# if value in di.values():
#     print(value,'is present in the dictionary')
# else:
#     print('not present')

# state=input('enter the state ')
# di['state']=state
# print(di)

