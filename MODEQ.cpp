#include<iostream>
using namespace std;
#define ll long long

ll fun(ll n, ll m){
	ll count = 0;
	for(ll a=1;a<n;a++){
		if (a==1){
			count+= n-1;
		}
		else{
			ll x1 = m%a;
			for(ll b = a+1;b<n+1;b++){
				ll x2 = (m%b)%a;
				if(x1==x2){
					count+=1;
				}
			}
		}
	}
	return count;
}


int main(){
	ll t,n,m;
	cin>>t;
	for(ll i=0;i<t;i++){
		cin>>n>>m;
		cout<<fun(n,m)<<endl;
	}
	
	
	return 0;
}
