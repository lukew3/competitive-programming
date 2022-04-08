#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main() {
	string x, s;
	cin >> x >> s;
	long long v = 0;
	if (s.length()%2 != 0) {
		v += s[0] - '0';
		s = s.substr(1);
	}
	for (int i=0; i<s.length()/2; i++) {
		v += stoi(s.substr(i*2, i*2+2));
	}
	cout << abs(v) % 11 << endl;
}
