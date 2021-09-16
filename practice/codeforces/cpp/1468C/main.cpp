#include <iostream>

using namespace std;

int main() {
	int q;
	cin >> q;

	int cust[q] = {0};
	int op, cval, loc, high, j, k;
	int cnum = 0;
	while(q--) {
		cin >> op;
		if(op == 1) {
			cin >> cval;
			cust[cnum] = cval;
			++cnum;
		} else if(op == 2) {
			for(j = 0; j < cnum; j++) {
				if(cust[j] > 0) {
					loc = j;
					break;
				}
			}
			cust[loc] = 0;
			++loc;
			cout << loc << " ";
		} else if(op == 3) {
			high = 0;
			for(k = 0; k < cnum; k++) {
				if(cust[k] > high) {
					loc = k;
					high = cust[k];
				}
			}
			cust[loc] = 0;
			++loc;
			cout << loc << " ";
		}
	}
}
