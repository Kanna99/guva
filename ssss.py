a=int(input())
b=int(input())
c=int(input())
if (a>b and a>c):
    print("a is greater")
elif (b>c and b>a):
    print("b is not greater")
elif (a==b and b==c):
    print("a,b,c is same")
else:
    print("c is greater")
