#include <bits/stdc++.h>

using namespace std;

void solve() {
	int n, d; cin >> n >> d;
	int a[n];
	int temp;
	for(int i=0; i<n; i++){
		cin >> temp;
		a[i] = temp;
	}
	std::sort(a);
	if(a[0]+a[1]< d || a[0] < d)
		cout << "YES" << endl;
	else
		cout << "NO" << endl;
}

int main() {
	int t; cin >> t;
	while (t--) solve();
}
