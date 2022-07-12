#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int tc=0; tc<t; tc++) {
		int n, v;
		v = 0;
		cin >> n;
		int a[n];
		for (int i=0; i<n; i++) {
			cin >> a[i];
		}
		for (int i=0; i<n; i++) {
			if (i+1 > a[i]) {
				for (int j=i+1; j<n; j++) {
					if (a[j] > i+1 && j+1 > a[j] && a[j] > i+1) {
						v++;
					}
				}
			}
		}
		cout << v << endl;
	}
	return 0;
}
