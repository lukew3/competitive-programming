#include <iostream>
#include <string>

using namespace std;

int main() {
	int n;
	string s;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> s;
		if (i%2 == 0)
			cout << s << endl;
	}
}
