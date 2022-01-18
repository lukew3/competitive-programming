#include <iostream>

using namespace std;

int main() {
	int dwarves[9];
	int sum = 0;
	for (int i = 0; i < 9; i++) {
		cin >> dwarves[i];
		sum += dwarves[i];
	}
	for (int i = 0; i < 8; i++) {
		for (int k = i+1; k < 9; k++) {
			if (sum - dwarves[i] - dwarves[k] == 100) {
				for (int l = 0; l < 9; l++) {
					if (l != i && l != k)
						cout << dwarves[l] << endl;
				}
				return 0;
			}
		}
	}
}
