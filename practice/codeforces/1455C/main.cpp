#include <iostream>

using namespace std;

void predictWins() {
	//Alice and Bob's stamina
	int x, y;
	//Alice and Bob's scores
	int a = 0;
	int b = 0;
	cin >> x;
	cin >> y;

	bool aliceServes = true;
	bool aliceReturn;
	while((x > 0) || (y > 0)) {
		//simulate a round
		//serve is deducted
		if(aliceServes == true) {
			if(x >0) {
				//cout << "Alice serves" << endl;
				x--;
				aliceReturn = false;
			} else {
				aliceServes = false;
				continue;
			}
		} else if(aliceServes == false) {
			if(y > 0) {
				//cout << "Bob serves" << endl;
				y--;
				aliceReturn = true;
			} else {
				aliceServes = true;
				continue;
			}
		}
		//decide how many returns are made
		bool roundOver = false;
		while(roundOver == false) {
			if(aliceReturn == true) {
				if(x > y) {
					x--;
					aliceReturn = false;
					//cout << "Alice hits" << endl;
				} else {
                                        roundOver = true;
                                        b++;
                                        aliceServes = false;
					//cout << "Alice waits" << endl;
				}
			} else if(aliceReturn == false) {
				if(y > x) {
					y--;
					aliceReturn = true;
					//cout << "Bob hits" << endl;
				} else {
					roundOver = true;
					a++;
					aliceServes = true;
					//cout << "Bob waits" << endl;
				}
			}
		}
	}
	cout << a << " " << b << "\n";
}

int main() {
	int t;
	cin >> t;
	for(int i=0; i<t; i++) {
		predictWins();
	}
}
