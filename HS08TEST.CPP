#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;

int main(){
	
	int a;cin>>a;
	float b,m;cin>>b;
	if(a%5==0&&b>=a+0.50)m=b-a-0.50;
	else m=b;
	cout<<fixed<<setprecision(2)<<m;
	
return 0;
}
