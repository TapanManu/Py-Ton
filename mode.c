#include<stdio.h>
void main()
{
int a[10],count=1,newcount=1,ccount=1,i,j,n;
printf("\tenter the size of the array\n");
scanf("%d",&n);
printf("\treading elements into the array\n");
for(i=0;i<n;i++)
{
	scanf("%d",&a[i]);
}
//find the largest number of repeating element
for(i=0;i<(n-1);i++)
{	newcount=1;
	for(j=i+1;j<n;j++)
	{ 
		if(a[i]==a[j])
		{
			newcount++;
		}
	}
	if(newcount>=count)
	{
		count=newcount;
	}
}
printf("count is:%d\n",count);
//find the mode
if(count==1)
{
	printf("mode does not exist");
}
else
{	
for(i=0;i<(n-1);i++)
{	ccount=1;
	for(j=i+1;j<n;j++)
	{ 
		if(a[i]==a[j])
		{
		ccount++;	
		}
	}
	if(ccount==count)
	{
	printf("mode is:%d\n",a[i]);
	}

}
}

}//end of pgm	
		
