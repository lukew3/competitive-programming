#include <bits/stdc++.h>
#include <string>

using namespace std;

void solve() {
	string s, t; cin >> s >> t;
	//multiply the shorter one until it is longer than the longer one
	//once they are the same length, test equivalency
	string temps = s;
	string tempt = t;
	while(temps.length() < 420) {
		if(temps == tempt) {
			cout << temps << endl;
			return;
		}if(temps.length() < tempt.length()) {
			temps += s;
		} else if(tempt.length() < temps.length()) {
			tempt += t;
		} else if(tempt.length() == temps.length()) {
			cout << -1 << endl;
			return;
		}
	}
}

int main() {
	int q; cin >> q;
	while (q--) solve();
}
