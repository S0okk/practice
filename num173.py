def div(x):
    a = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            a.add(i)
            a.add(x//i)
    return sorted(a)

def prost(x):
    return all(x%i!=0 for i in range(2,int(x**0.5)+1))
for x in range(650_001,651_000):
    li = [i for i in div(x) if prost(i)]
    if len(li)>0:
        f = int(sum(li)/len(li))
        if f%37==23:
            print(x,f)