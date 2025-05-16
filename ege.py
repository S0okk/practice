# s = open('k7b-3.txt').readline()
# print(len('BAFE' * 7 + 'BAF'))

# s = open('k7b-6.txt').readline()
# print(len('DAF' * 56 + 'D'))

# s = open('24-171.txt').read()
# print(len('Z'+'XYZ'*17 + 'Z')) ########

# s = open('24-197.txt').readline()
# s = s.replace('ZXY', '*').replace('ZYX', '*')
# for letter in s:
#     if letter != '*':
#         s = s.replace(letter, ' ')
# s = s.split()
# print(max(len(x) for x in s))

# s = open('24-215.txt').readline()
# s = s.replace('B', 'A').replace('C', 'A').replace('2', '1').replace('3', '1')
# s = s.replace('A1', '*')
# for x in s:
#     if x != '*':
#         s = s.replace(x, ' ')
# s = s.split()
# print(max(len(i) for i in s))

s = open('24-215.txt').readline()
c=0
ma = 0
for letter in 'BC':
    s=s.replace(letter, 'A')
for letter in '23':
    s=s.replace(letter, '1')
for i in range(len(s)-2):
    if s[i] + s[i+1] + s[i+2] == 'A1A':
        c+=1
        ma = max(ma, c)
    elif c != 0:
        c = 0
print(ma)

# from string import printable
# s = open('24-279.txt').readline()
# alf = printable[:10] + printable[36:42]
# for i in s:
#     if i not in alf:
#         s=s.replace(i, ' ')
# s = s.split()
# print(max(len(x) for x in s if x[0] != '0'))

# s = open('24-153.txt').readline()
# for i in 'ABCEF':
#     s = s.replace(i, ' ')
# s = s.split()
# print(min(len(i) for i in s))