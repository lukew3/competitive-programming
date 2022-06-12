#include <bits/stdc++.h>
#include <string>

using namespace std;

void solve() {
	int n, m; cin >> n >> m;
	string p; cin >> p;
	for(int i=0; i<m; i++) {
		int x = 0;
		int l, r; cin >> l >> r;
		string p2 = p.substr(0,l-1) + p.substr(r, p.length());
		int count = 0;
		for(int j=0; j<(p2.length()); j++) {
			if(p2[j] == '+') {
				x++;
			} else if(p2[j] == '-') {
				x--;
			}
		}
		cout << upper-lower+1 << endl;
	}	
}

int main() {
	int t; cin >> t;
	while (t--) solve();
}
