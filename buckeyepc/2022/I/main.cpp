#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main() {
	string x, s;
	cin >> x >> s;
	int v = 0;
	for (int i=0; i<s.length(); i++) {
		if (i%2 == 0) v += s[i] - '0';
		else v -= s[i] - '0';
	}
	cout << abs(v) % 11 << endl;
}
