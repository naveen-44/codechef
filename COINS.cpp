#include<iostream>
using namespace std;
#define ll long long

int maxim(a,b){
  if(a>b){
    return a;
  }
  return b;
}

int main(){
  ll n = 0;
  while(cin>>n){
    cout<<maxim(n,n/2 + n/3 + n/4)<<endl;
  }

  return 0;
}
