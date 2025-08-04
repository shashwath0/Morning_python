# class A:
#     x=10
# class B(A):
#     y=20
# b=B()
# print(b.x)
# print(b.y)
# print('\n')
#
# class A:
#      x=10
# class B(A):
#      y=20
# class C(B):
#      z=30
# c=C()
# print(c.x)
# print(c.y)
# print(c.z)
# print('\n')
#
# class A:
#     x=10
#     k=50
# class B(A):
#     y=20
# class C(A):
#     z=30
# b=B()
# print(b.x)
# print(b.y)
# c=C()
# print(c.k)
# print(c.z)
# print('\n')
#
# class A:
#      x=10
# class B:
#      y=20
# class C(A,B):
#      z=30
# c=C()
# print(c.z)
# print(c.y)
# print(c.x)
# print('\n')

# class A:
#     def m1(self):
#         print('hi')
# class B(A):
#     def __init__(self):
#         print(super().m1)
#         print('bye')
# b=B()