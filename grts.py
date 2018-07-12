N=int(input())
a=[]
if N<=1000000:
    n=raw_input()
    a.extend([int(x) for x in n.split()])
    a.sort(reverse=True)
    u=""
    for i in range(len(a)):
                   u=u+str(a[i])
    print(u)
