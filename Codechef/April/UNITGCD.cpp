#include<bits/stdc++.h>
using namespace std;
int main () 
{
    int t;
    cin>>t;
    while(t--) 
    {
        int n;
        cin >> n;
        if(n>=2) // check to see if less cases make it faster
            cout<<n/2<<"\n";
        else
            cout<<1<<"\n";
        if(n>=4)
        {
            cout <<"3 1 2 3"<<"\n"; //day 1 
            int i,j;
            for(i=4, j=1 ; j<n/2; i+=2, j++) //don't forget j 
            {
                if(i==n)
                    cout<<1<<" "<<i<<" ";
                else
                    cout<<2<<" "<<i<<" ";
                if(i!=n) 
                    cout << i + 1 << "\n";
                else 
                    cout<<"\n";
            }
        }
        else // let's see if it runs faster
        {
            cout <<n<<" ";
            for(int i = 1; i <=n; i++)
                cout <<i<<" ";
            cout << "\n";
        } 
    }
    return 0;
}