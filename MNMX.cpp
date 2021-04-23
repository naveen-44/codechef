#include<iostream>
#define in long long
using namespace std;
int main(){
	in t;cin>>t;
	while(t--){
		in n;cin>>n;
		in a[n],min=1000000,mp=0,sum=0;
		for(in i=0;i<n;i++){
		cin>>a[i];
		if(min>a[i])min=a[i];
	}
	cout<<(n-1)*min<<endl;
}
	return 0;
}
