#include<stdio.h>

void main()

{
	
int a,b,c,d;
	
char m[10],n[10];
scanf("%s",&m);

scanf("%s",&n);

for(a=0;m[a]!='\0';a++)

{
		
if(m[a]==n[a])
		
{
		
printf("%c",m[a]);
		
}
		
else
		
{
		
break;
		
}
	
}

}