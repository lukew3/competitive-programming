#include <iostream>

using namespace std;

int main() {
	int m, n;
	cin >> m;
	cin >> n;

	//if one side is divisible by two, just divide it by two and multiply the answer by the other value
	//if not, divide a side by two and add length/2 to the solution
	int answer;
	if((m % 2) == 0) {
		answer = n * (m / 2);
	} else if((n % 2) == 0) {
		answer = m * (n / 2);
	} else {
		answer = (n * (m/2)) + (n/2);
	}
	cout << answer;
}
