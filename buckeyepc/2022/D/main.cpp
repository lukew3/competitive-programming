#include <iostream>
#include <math.h>

using namespace std;

int main() {
	int n, t;
	double part = 0;
	cin >> n;
	cin >> t;
	double total = n * n;
	for (int i=1;i<=n;i++) {
		for (int j=1;j<=n;j++) {
			if (j+i == t) part++;
		}
	}
	cout << round(part*1000/total) << '/' << 1000 << endl;
}
