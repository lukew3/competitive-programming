#include <iostream>

using namespace std;


int solve() {
	int count = 0;
	int temp;

	for(int j = 0; j < 3; j++) {
		cin >> temp;
		count += temp;
	}

	if(count >= 2) {
		return 1;
	} else {
		return 0;
	}
}

int main() {
	int n;
	cin >> n;
	
	int aggreed_count = 0;
	for(int i = 0; i < n; i++) {
		aggreed_count += solve();
	}
	cout << aggreed_count;
}
