#include <bits/stdc++.h>
#define pb push_back
#define fi first
#define se second
#define all(v) v.begin(),v.end()
#define ll long long
#define VII vector<int>
#define VLL vector<ll>
#define VVII vector<VII>
#define fl(i,a,n) for(__typeof(a) i=a;i<n;i++)
#define flk(i,a,n,k) for(__typeof(a) i = a; i<n; i+=k)
#define flinv(i,n,a,k) for(__typeof(n) i = n; i>a; i-=k)
#define fliter(it,a) for(__typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define pi 3.141592653589793
#define MPCI map<int,char>
const int MOD = 1e9+7;
const int INF = 1e9;
using namespace std;

int profit(VVII vct){
    MPCI mp12,mp3,mp6,mp9;
    fl(i,0,4){//column wise
        fl(j,0,4){//row wise
            if(i == 0){
                mp12[vct[j][i]] = j;
            }else if(i == 1){
                mp3[vct[j][i]] = j;
            }else if(i == 2){
                mp6[vct[j][i]] = j;
            }else{
                mp9[vct[j][i]] = j;
            }
        }
    }
    int count = 0,profitval = 0 ;
    while(1){
        int t12,t3,t6,t9;
        t12 = (mp12.rbegin()->first);
        t3 = (mp3.rbegin()->first);
        t6 = (mp6.rbegin()->first);
        t9 = (mp9.rbegin()->first);
        if()
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
	int t;
	ll totalprofit = 0;
	cin >>t;
	fl(i,0,t){
        //let's go
        ll profit=0;
        VVII vct;
        int N,t;
        cin >>N;
        vct.resize(4);
        fl(k,0,4){
            vct[k].resize(4);
            fill(vct[k].begin(),vct[k].end(),0);
        }
        fl(j,0,N){
            char ch;
            cin >>ch>>t;
            if(t == 12){
                vct[ch-'A'][0] += 1;
            }else if(t == 3){
                vct[ch-'A'][1] += 1;
            }else if(t == 6){
                vct[ch-'A'][2] += 1;
            }else{
                vct[ch-'A'][3] += 1;
            }
        }
        
	}
	return 0;
}
