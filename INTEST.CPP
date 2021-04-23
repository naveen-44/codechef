#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;
#define ll long long
int main(){
	ll count=0;
	ll n,k;cin>>n>>k;
	for(ll i=0;i<n;i++){
		ll a;cin>>a;
		if(a%k==0)count++;
	}
	cout<<count;
	
return 0;
}
