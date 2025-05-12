s = 'babad'
max_pal = ''
while s != '':
    for i in range(len(s)):
        s2 = s[i::-1]
        if s[:i+1] == s2:
            if len(s[i::-1]) > len(max_pal):
                max_pal = s[i::-1]
    s = s[1:]
print(max_pal)