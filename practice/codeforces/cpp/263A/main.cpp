#include <iostream>

using namespace std;

int main() {
	int myarr[5][5];
	int temp;
	int x;
	int y;

	for(int i = 0; i < 5; i++) {
		for(int j = 0; j <5; j++) {
			cin >> temp;
			if(temp == 1) {
				x = i;
				y = j;
				goto break_nested;
			}
		}
	}
	break_nested:
	cout << (abs(2-x) + abs(2-y));
}
