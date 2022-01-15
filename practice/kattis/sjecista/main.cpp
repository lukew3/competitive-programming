#include <iostream>

using namespace std;

int main() {
	int n, s = 0;
	cin >> n;
	for(int i = 1; i < n-2; i++) {
		for (int j = 0; j < i+1; j++) {
			s += (j+1) * (i-j);
		}
	}
	cout << s << endl;
}
