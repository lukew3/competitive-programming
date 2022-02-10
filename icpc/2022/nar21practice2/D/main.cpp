#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int simgame(int ladders[64][2], int target, int k) {
	int pos = 0, rc = 0;
	while (true) {
		pos += rand() % 6 + 1;
		rc+=1;
		for(int i=0; i<k; i++) {
			cout << ladders[i][0] << ladders[i][1] << endl;
			if (ladders[i][0] == pos) {
				pos = ladders[i][1];
				break;
			}
		}
		if (pos >= target) {
			return rc;
		}
	}
}

void solve(int target, int ladders[64][2], double p, int k) {
	int games = 10000000;
	int gamearr [64];
	for(int i=0; i<64; i++) gamearr[i] = 0;
	for(int i=0; i<games; i++) {
		gamearr[simgame(ladders, target, k)]++;
	}
	int lastsum = 0;
	int testval = games*p;
	for(int i=0; i<64; i++) {
		cout << gamearr[i] << endl;
		lastsum += gamearr[i];
		if (lastsum >= testval) {
			cout << i << endl;
			return;
		}
	}
}

int main() {
	srand(time(NULL));
	int r, c, k;
	double p;
	cin >> r >> c >> k;
	cin >> p;
	int target = r * c;
	int ladders [k][2];
	for(int i = 0; i < k; i++) {
		cin >> ladders[i][0] >> ladders[i][1];
	}
	solve(target, ladders, p, k);
}
