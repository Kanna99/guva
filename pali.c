#include<stdio.h>
int main()
{
	int i,n,rev=0;
	scanf("%d",&n);
	n=i;
	while(i>0)
	{
		rev=rev*10;
		rev=rev+i%10;
		i=i/10;
	}
	if(n==rev)
	printf("it is palindrome");
	else
        printf("it is not a palindrome"); 
return 0;
}