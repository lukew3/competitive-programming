#include <iostream>

using namespace std;

int main() {
	int n;
	int k;

	cin >> n;
	cin >> k;
	int scores[n];

	for(int i = 0; i < n; i++) {
		int score;
		cin >> score;
		scores[i] = score;
	}
	
	int target_score = scores[k-1];
	int answer = 0;

	for(int j = 0; j < n; j++) {
		if ((scores[j] > 0) && (scores[j] >= target_score)) {
			answer++;
		}
	}
	cout << answer;
}
