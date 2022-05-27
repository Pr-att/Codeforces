# TODO: Not Completed.

for i in range(int(input())):
    a, b = map(int, input().split())
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    p, q, r, s = sorted(n), sorted(m), tuple(n), tuple(m)
    count = 0
    u = []
    for j in range(len(n)):
        for k in range(j + 1, len(m)):
            try:
                if n[j] >= n[k] and m[j] >= m[k]:
                    count += 1
                    n[j], m[j], n[k], m[k] = n[k], m[k], n[j], m[j]
                if n == p and m == q:
                    u.append((j + 1, k + 1))
                    break
                else:
                    n, m = list(r), list(s)
            except IndexError:
                break
    if n != p:
        print(-1)
    elif count == 0:
        print(1, 1)
    else:
        print(u[0][0], u[0][1])

"""

#include <iostream>
#include <string>
#include <sstream>
#include <iomanip> 
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <functional>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <complex>
#include <numeric> 

using namespace std;

//#pragma GCC optimize("Ofast")
//#pragma GCC optimization("unroll-loops, no-stack-protector")
//#pragma GCC target("avx,avx2,fma")


typedef long long LL;
typedef pair<LL, LL> PL;
typedef vector<LL> VL;
typedef vector<PL> VPL;
typedef vector<VL> VVL;

typedef pair<int, int> PI;
typedef vector<int> VI;
typedef vector<PI> VPI;
typedef vector<vector<int>> VVI;
typedef vector<vector<PI>> VVPI;

typedef long double LD;
typedef pair<LD, LD> PLDLD;

typedef complex<double> CD;
typedef vector<CD> VCD;

#define MP make_pair
#define PB push_back
#define F first
#define S second
#define LB lower_bound
#define UB upper_bound

#define SZ(x) ((int)x.size())
#define LEN(x) ((int)x.length())
#define ALL(x) begin(x), end(x)
#define RSZ resize
#define ASS assign
#define REV(x) reverse(x.begin(), x.end());

#define MAX(x) *max_element(ALL(x))
#define MIN(x) *min_element(ALL(x))
#define FOR(i, n) for (int i = 0; i < n; i++) 
#define FOR1(i, n) for (int i = 1; i <= n; i++) 
#define SORT(x) sort(x.begin(), x.end())
#define RSORT(x) sort(x.rbegin(), x.rend())
#define SUM(x) std::accumulate(x.begin(), x.end(), 0LL)


#define IN(x) cin >> x;
#define OUT(x) cout << x << "\n";
#define INV(x, n) FOR(iiii, n) { cin >> x[iiii]; }
#define INV1(x, n) FOR1(iiii, n) { cin >> x[iiii]; }
#define OUTV(x, n) { FOR(iiii, n) { cout << x[iiii] << " "; } cout << "\n"; }
#define OUTV1(x, n) { FOR1(iiii, n) { cout << x[iiii] << " "; } cout << "\n"; }
#define OUTYN(x) { if (x) cout << "YES\n"; else cout << "NO\n"; }
#define OUTyn(x) { if (x) cout << "Yes\n"; else cout << "No\n"; }


const LL INF = 1E18;
const int MAXX = 200005;
const LD PAI = 4 * atan((LD)1);

#define MOD7 1000000007
#define MOD9 1000000009
#define MOD3 998244353



int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	LL t, n, m, i, j, k;
	cin >> t;
	while (t--) {
		cin >> n >> m;
		VVL a(m, VL(n)), aa;
		FOR(i, n) {
			FOR(j, m) cin >> a[j][i];
		}
		aa = a;
		SORT(aa);

		VL ans;
		FOR(i, m) {
			if (a[i] != aa[i]) ans.push_back(i + 1);
		}

		if (ans.empty()) {
			ans.push_back(1);
			ans.push_back(1);
		}

		FOR(i, n) {
			FOR1(j, m - 1) {
				if (aa[j][i] < aa[j - 1][i]) ans.clear();
			}
		}

		if (ans.size() != 2) OUT(-1)
		else OUTV(ans, 2);
	}

	return 0;
}

"""
