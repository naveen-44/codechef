#include<iostream>
#include<math.h>
using namespace std;
#define ll long long

int main()
{int t=0,k;
 cin>>t;
 for(k=0;k<t;k++)
 {
 	
	 
 int n,a[500],index=0,temp,i;	
 		a[0]=1;
 		//cout<<"enter num"<<endl;
 		cin>>n;
 		for(;n>1;n--)
 		{
 			temp=0;
 			for(i=0;i<=index;i++)
 			{
 				temp=(a[i]*n)+temp;
 				a[i]=temp%10;
 				temp=temp/10;
			 }
			 while(temp>0)
			 {
			 	a[++index]=temp%10;
			 	temp=temp/10;
			 }
		 }
 		for(i=index;i>=0;i--)
 		{
 			cout<<a[i];
		 }cout<<endl;
	}
	return 0;
}
