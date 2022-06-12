#include <iostream>

using namespace std;

void solve() {
	int a, b, c;
	cin >> a >> b >> c;
	int total = a + b + c;
	if (((total % 9) == 0) && (total/9 <= a) && (total/9 <= b) && (total/9 <= c))
		cout << "YES\n";
	else
		cout << "NO\n";
}

int main() {
	int t;
	cin >> t;
	while(t--) solve();
}
