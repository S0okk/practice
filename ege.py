# s = open('k7-29.txt').readline()
# s = s.replace('A', ' ').replace('B', ' ')
# s = s.split()
# print(max([len(x) for x in s]))

# s = open('k7-45.txt').readline()
# s = s.replace('A', ' ').replace('B', ' ')
# s = s.split()
# print(max([len(x) for x in s]))

# s = open('k7a-3.txt').readline()
# s = s.replace('C', ' ').replace('D', ' ')
# s = s.split()
# print(max([len(x) for x in s])) ###############

# s = open('k7a-5.txt').readline()
# s = s.replace('C', ' ').replace('F', ' ')
# s = s.split()
# print(max([len(x) for x in s]))

# s = open('k7c-3.txt').readline()
# c = 0
# for i in range(len(s) - 2):
#     if s[i+1] in 'BDE':
#         if s[i+2] in 'ACD' and s[i+2] != s[i+1]:
#             if s[i] == s[i+2]:
#                 c += 1
# print(c)

# s = open('k8-6.txt').readline()
# c = 1
# ma = 0
# st = ''
# while s != '':
#     for i in range(len(s) - 1):
#         if s[i] == s[i+1]:
#             c += 1
#             if c > ma:
#                 ma = c
#                 st = s[i]
#         else:
#             c = 1
#     s = s[1:]
# print(st, ma)
