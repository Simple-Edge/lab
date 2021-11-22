# 1.
# def calc():
#     while True:
#         symbol = input('type math operation symbolbol: + - % / *: ')
#         x = int(input('type 1 num: '))
#         y = int(input('type 2 num: '))
#         if symbol == '+':
#             print(x+y)
#             break
#         elif symbol == '-':
#             print(x-y)
#             break
#         elif symbol == '%':
#             print(x%y)
#             break
#         elif symbol == '/':
#             print(x/y)
#             break
#         elif symbol == '*':
#             print(x*y)
#             break
#         else:
#             print('try again')
# calc()

# 2.
# def S(a,b):
#     print(f'S = {0.5*a*b}')
# S(11,1)

# 3.
# def shushp(h1,h2,h3,h4):
#     print(f'((h1-h1%3)/3+1)+((h2-h2%3)/3+1)+((h3-h3%3)/3+1)+((h4-h4%3)/3+1)')
# shushp(4,1,1,1)

# 4.
# age = int(input('type your age: '))
# height = int(input('type your height: '))
# gender = input('type your gender: ')
# name = input('type your name: ')
# surename = input('type your surename: ')
# print(f"age: {age}\nheight: {height}\ngender: {gender}\nname: {name}\nsurename: {surename}")

# 5.
# def reverseClock():
#     h = 0
#     m = 0
#     while True:
#         h = int(input('type hours max 24: '))
#         if h>24:
#             print('try again')
#         else:
#             break
#     while True:
#         m = int(input('type minutes if hours = 24 minutes can be only 00 in other cases max is 59: '))
#         if h == 24 and m != 0 or m > 59:
#             print('try again')
#         else:
#             break
#     part = int(input('type part of task 1,2: '))
#     if part == 1 :
#         print(f'{h*60+m}')
#     elif part == 2 :
#         print(f'{h*3600+m*60}')
# reverseClock()

# 6.
# while True:
#     d = input('type nums with spaces: ')
#     if d.replace(' ','1').isnumeric() and d.count(' ') == 2:
#         x = d.split()
#         break
#     else:
#         print('try again')
# print(f'{int(x[0])+int(x[1])}')

# 7. 
# x=int(input("x: "))
# y=int(input('y: '))
# d=[x,y]
# z=0
# if d[0] == 0 or d[1] == 0:
#     print('Error')
# elif d[0] % 2 == 0 and d[1] % 2 == 0:
#     for x in range(2,max(d)+1,2):
#         if d[0] % x == 0 and d[1] % x == 0:
#             z = x
# else:
#     for x in range(1,max(d)+1,2):
#         if d[0] % x == 0 and d[1] % x == 0:
#             z = x
# print(f'highest divider:{z}')

# 8.
# x1 = int(input('x1: '))
# x2 = int(input('x2: '))
# y1 = int(input('y1: '))
# y2 = int(input('y2: '))
# print(f'{((x1-x2)**2+(y1-y2)**2)**0.5}')






