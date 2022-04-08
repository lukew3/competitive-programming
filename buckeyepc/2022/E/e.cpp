#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main() {
	int s, l;
	cin >> s >> l;
	string m;
	cin >> m;
	int best = -1;
	for (int i=0; i<s; i++) {
		for (int j=i+1; j<min(i+l,s); j++) {
			cout << j
			int v = stoi(m.substr(i,j));
			bool isPrime = true;
			for (int k=2; k<sqrt(v); k++) {
				if (v%k == 0) {
					isPrime = false;
					break;
				}
			}
			if (isPrime && v > best) best = v;
		}
	}
	if (best == -1) {
		cout << "No Primes" << endl;
	} else {
		cout << best << endl;
	}
}
