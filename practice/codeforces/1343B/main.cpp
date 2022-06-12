#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for(int i = 0; i < t; i++) {
		int n;
		cin >> n;
		if((n % 4) == 0) {
			cout << "YES" << endl;
			int myarr[n];
			for(int j = 0; j < (n - 1); j++) {
				if(j < (n/2)) {
					myarr[j] = (2 * j) + 2;
				} else {
					myarr[j] = (2 * (j-(n/2))) + 1;
				}
			}
			myarr[n-1] = n + 2 * ((n/4)-1) + 1;
			for (int k=0; k < n; k++) {
				cout << myarr[k] << " ";
			}
			cout << endl;
		} else {
			cout << "NO" << endl;
		}
	}
}
