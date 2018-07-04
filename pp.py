a=input()
b=input()
for m in range(a,b+1):
    if m>1:
       for i in range(2,m):
           if(m%i==0):
              break
    else:
       print(m)