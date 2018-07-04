num=int(input())
if num>1:
     for i in range(2,num):
         if num%i==0:
            print(num,"it is not prime")
            break
         else:
            print(num,"its a prime")
else:
   print(num,"it not prime")