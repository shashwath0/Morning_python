# li=[]
# i=0
# while i<=100:
#     li.append(i)
#     i=i+2
# print(li)

# li=[1,5,6,8,3]
# n_li=[]
# for i in range(5):
#     if i%2==0:
#       n_li.append(li[i]*5)
# print(n_li)

# li=[1,5,6,8,3]
# y=[]
# for i in range(len(li)):
#     if i%2==1:
#         y.append(li[i]**2)
# print(y)

# li=[1,5,6,8,3]
# y=[]
# for i in li:
#         y.append(i*2)
# print(y)

# li=[1,5,6,8,3]
# y=[li[i]**2 for i in range(len(li))if i%2==1]
# print(y)
# y=[li[i]*5 for i in range(len(li))if i%2==0]
# print(y)
# y=[i*2 for i in li]
# print(y)

# li=[11,3,6,10,13]
# y=[li[i]**2 for i in range(len(li))if li[i]%3==0]
# print(y)
# y=[i+5 for i in li]
# print(y)
# y=[li[i]**2 for i in range(len(li))if li[i]>=10]
# print(y)

# x=['hi','python','we','write','python','we','say','hi','python']
# y={}
# for i in x:
#     if i in y.keys():
#         y[i]=y[i]+1
#     else:
#         y[i]=1
# print(y)

# x=[('a',10),('b',20),('c',30),('d',40)]
# for i in range(4):
#     print(x[i][1],end=' ')

# x=['a','b','c','d']
# y=[10,20,30,40]
# di={}
# for i in range(4):
#     di[x[i]]=y[i]
# print(di)

# x=['a','b','c','d']
# y=[10,20,30,40]
# li=[]
# for i in range(4):
#     li.append((x[i],y[i]))
# print(li)

# x=10
# def f1():
#     x=20
#     print(x)
#     print(globals()['x'])
# f1()

# x=10
# y=20
# def f1():
#     y=30
#     print(x)
#     print(y)
#     print(globals()['x'])
#     print(globals()['y'])
# f1()

