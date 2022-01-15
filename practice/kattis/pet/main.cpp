#include <iostream>

using namespace std;

int main() {
	int a, b, c, d, score, winner, winnerScore = 0;
	for(int i = 0; i < 5; i++) {
		cin >> a >> b >> c >> d;
		score = a + b + c + d;
		if (score > winnerScore) {
			winner = i + 1;
			winnerScore = score;
		}
	}
	cout << winner << ' ' << winnerScore << endl;
}
