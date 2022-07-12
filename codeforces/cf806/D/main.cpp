#include <iostream>
using namespace std;

void solve() {
	int n;
	cin >> n;
	int s[n] = {0};
	int b[n] = {0};
	for (int i=0; i<n; i++) {
		cin >> s[i];
	}
	for (int j=0; j<n; j++) { for (int k=0; k<n; k++) {
			for (int i=0; i<n; i++) {
				if (i != j and i != k and s[i] == s[j] + s[k]) {
					b[i] = 1;
				}
			}
		}
	}
	for (int i=0; i<n; i++) {
		cout << b[i];
	}
	cout << endl;
}

int main() {
	int t;
	cin >> t;
	for(int tt; tt<t; tt++) {
		solve();
	}
	return 0;
}
