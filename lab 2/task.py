# 1.
# while True:
#     d = input('type nums with spaces: ')
#     if d.replace(' ','1').isnumeric() and len(d.split()) == 3:
#         f = d.split()
#         print(f'Max num {max(int(f[0]),int(f[1]),int(f[2]))} \nMin num {min(int(f[0]),int(f[1]),int(f[2]))}')
#         break
#     else:
#         print('try again')

# 2.
# import re
# while True:
#     d = input('type equation like in example: ax**2+bx+c=0 where a,x=integers : ')
#     if d.replace('+','1').replace('=','2').replace('x','3').replace('**','4').isnumeric() and len(d.split('+')) == 3 and d.split('+')[0].count('x') == 1 and d.split('+')[0].count('*') == 2 and d.split('+')[1].count('x') == 1 and d.split('+')[1].count('*') == 0 and re.split('[+ =]',d)[2].isnumeric():
#         f = re.split('[+ =]',d.replace('**','!'))
#         a = int(f[0][0:-3])
#         b = int(f[1][0:-1])
#         c = int(f[2])
#         d = b**2-4*a*c
#         if d > 0 :
#             print('2 roots')
#         elif d == 0 :
#             print('1 roots')
#         elif d < 0 :
#             print('no roots')
#         break
#     else:
#         print('try again')
# # 12345x**2+2x+10=0

# 3.
# while True:
#     z = []
#     d = input('type 2 digit number: ')
#     if d.isdigit() and int(d) < 100 and int(d) > -100:
#         d = int(d)
#         if d == 0 :
#             print('0')
#         elif d % 2 == 0 :
#             for x in range(2,d+1,2):
#                 if d % x == 0 :
#                     z.append(x)
#         else:
#             for x in range(1,d+1,2):
#                 if d % x == 0 :
#                     z.append(x)
#         print(z)
#         break
#     else:
#         print('try again')

# 4.
# while True:
#     d = input('type 3 nums with spaces: ')
#     if d.replace(' ','1').isnumeric() and len(d.split()) == 3:
#         f = d.split()
#         if f.count(f[0]) == 2 or f.count(f[1]) == 2 or f.count(f[2]) == 2 :
#             print('2')
#         elif f.count(f[0]) == 3:
#             print('1')
#         else:
#             print('3')
#         break
#     else:
#         print('try again')

# 5.
# while True:
#     d = input('type  4 nums with spaces: ')
#     if d.replace(' ','1').isnumeric() and len(d.split()) == 4:
#         f = d.split()
#         even = []
#         odd = []
#         for d in f :
#             d = int(d)
#             if d % 2 == 0 :
#                 even.append(d)
#             elif d % 2 !=0 :
#                 odd.append(d)
#         print(f'even nums :{sorted(even)} \nodd nums:{sorted(odd)}')
#         break
#     else:
#         print('try again')

# 6.
# guestions =[
#     'fd',
#     'ef',
#     'fe',
#     'ef',
#     'ef'
# ]
# options =[
#     'f',
#     '',
#     '',
#     '',
#     '',
#     ''
# ]
# answers =[
#     'f'
#     '',
#     '',
#     '',
#     '',
#     ''
# ]
# length = min(len(options),len(guestions),len(answers))
# scoreT = 0
# for i in range (0,length) :
#     print(f'{guestions[i]}. please choose and write correct option on your mind')
#     d = input(f'{options[i]}:\n')
#     if answers[i] == d:
#         scoreT += 1
#         print(f'Correct')
#     else:
#         print(f'inorrect the answer was {answers[i]}')
# print(f'inorrect answers : {length - scoreT} \ncorect answers : {scoreT}')

# 7.
# guestions =[
#     'fd',
#     'ef',
#     'fe',
#     'ef',
#     'ef'
# ]
# options =[
#     'f',
#     '',
#     '',
#     '',
#     '',
#     ''
# ]
# answers =[
#     'f'
#     '',
#     '',
#     '',
#     '',
#     ''
# ]
# length = min(len(options),len(guestions),len(answers))
# scoreT = 0
# for i in range (0,length) :
#     print(f'{guestions[i]}. please choose and write correct option on your mind')
#     d = input(f'{options[i]}:\n')
#     if answers[i] == d:
#         scoreT += 1
# if scoreT == 40 :
#     print('you accepted on work')
# else:
#     print('WASTED')

# 8.
# name = input()
# surename = input()
# name2 = input()
# surename2 = input() 
# if name == name2 and surename == surename2:
#     print(f'ви у розшуку громодянин {name} {surename}')




