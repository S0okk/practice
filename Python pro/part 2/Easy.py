n = int(input())
li = []
for i in range (1,n+1):
    a = int(input())
    li.append(a)
last = li[0]
li2 = li.pop(0)
li2 = li2.append(last)
k=0
cur = int(input())
for num in li:
    for num2 in li2:
        print(num, num2)
        if num*num2 == cur:
            k+=1
print(k)
if k>0:
    print('ДА')
else:
    print('НЕТ')