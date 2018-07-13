a=int(input())
d=0
if (1<=a<=1000000000000000000):
    b=[int(x) for x in str(a)]
    print(b)
    for i in range(len(b)):
        c=b[i]*b[i]
        d=d+c
print(d)
      
