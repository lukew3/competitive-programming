#include <bits/stdc++.h>

using namespace std;

void solve() {
	int n, d; cin >> n >> d;
	int a[n];
	int lowest = -1;
	int low = -1;
	bool firstcond = true;
	for(int i=0; i < n; i++) {
		int temp; cin >> temp;
		if (temp > d)  firstcond = false;
		if (temp <= lowest || lowest == -1) {
			low = lowest;
			lowest = temp;
		} else if (temp <= low || low == -1) 
			low = temp;
	}
	//If all values are less than d or:
	//If the sum of the two lowest values is less than or equal to d 
	if(firstcond == true) {
		cout << "YES" << endl;
	} else if((low + lowest) <= d) {
		cout << "YES\n";
	} else {
		cout << "NO\n";
	}
}

int main() {
	int t; cin >> t;
	while (t--) solve();
}
