#include<stdio.h>
int main()
{
int n,i,rem,res=0;
printf("enter the number");
scanf("%d",&n);
n=i;
while(i!=0)
{
     rem=i%10;
     res+=rem*rem*rem;
     i/=10;
}
if(res==n)
printf("%d is armstrong ");
else
printf("%d is not armstrong ")
return 0;
}