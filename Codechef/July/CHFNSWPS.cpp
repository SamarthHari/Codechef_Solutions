#include<bits/stdc++.h>
#define int long long int
#define pb push_back
using namespace std;

signed main(){
 int t;
 cin>>t;
 while(t--)
 {
     int n;
     cin>>n;
     vector<int> a(n),b(n);
     map<int, int> m1,m2,m3,m4;
     for(int i=0;i<n;i++){
     cin>>a[i];
     m1[a[i]]++;
     }
     for(int i=0;i<n;i++){
     cin>>b[i];
     m2[b[i]]++;
     }
    int x=0;
    for(int i=0;i<n;i++){
        x=x^a[i];
        x=x^b[i];
    }
     if(x!=0)
        cout<<-1<<endl;
     else
     {
     	int cost=0;
     	int m=1000000000000000000;
     	for(int i=0;i<n;i++)
     	m=min(m,a[i]);
     	for(int i=0;i<n;i++)
     	m=min(m,b[i]);
        for(auto i:m1)
        {
            if(i.second>m2[i.first])
            m3[i.first]=(i.second-m2[i.first])/2;
        }
        for(auto i:m2)
        {
            if(i.second>m1[i.first])
            m4[i.first]=(i.second-m1[i.first])/2;
        }
        vector<int> v1,v2;
        for(auto i:m3)
        {
            for(int j=0;j<i.second;j++)
            v1.pb(i.first);
        }
        for(auto i:m4)
        {
            for(int j=0;j<i.second;j++)
            v2.pb(i.first);
        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end(),greater<int>());
        for(int i=0;i<v1.size();i++)
        {
        	int k1=v1[i];
        	int k2=v2[i];
        	cost+=min(2*m,(min(k1,k2)));
        }
        cout<<cost<<endl;
     }
 }
return 0;
}