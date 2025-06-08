def div(x):
    a = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            a.add(i)
            a.add(x//i)
    return sorted(a)

def prost(x):
    return all(x%i!=0 for i in range(2,int(x**0.5)+1))

for x in range(912672,350000,-1):
    li = [i for i in div(x) if not prost(i)]
    if x%2!=0 and len(li)!=0:
        s = sum(li)
        if x%s==0:
            print(x,s)