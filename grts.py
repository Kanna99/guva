N=int(input())
a=[]
if N<=1000000:
    n=raw_input()
    a.extend([int(x) for x in n.split()])
    a.sort(reverse=True)
    k=""
    for i in range(len(a)):
                   k=k+str(a[i])
    print(k)
