list=[int(x) for x in raw_input().split()]
a=[]
for num in range(len(list)):
    for i in range(num+1,len(list)):
        if(list[num]==list[+i]):
            a.append(list[num])
l=set[a]
for i in range(len(l)):
    print(l[i],end=" ")
