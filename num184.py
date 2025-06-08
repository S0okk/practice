def div(x):
    a = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            a.add(i)
            a.add(x//i)
    return sorted(a)

for x in range(300001,10**7):
    li = [i for i in div(x)]
    if len(li)>=5:
        p = li[0]*li[1]*li[2]*li[3]*li[4]
        if p<=x and p%100==31:
            print(p,li[4])
