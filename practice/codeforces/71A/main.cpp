#include <iostream>
#include <string>

using namespace std;

void solve() {
	string instr;
	string outstr;

	cin >> instr;
	outstr = instr;
	if(instr.length() > 10) {
		string inner = to_string(instr.length() - 2);
		outstr = instr[0] + inner + instr.back();
	}

	cout << outstr << endl;
}

int main() {
	int n;
	cin >> n;
	for(int i = 0; i < n; ++i) {
		solve();
	}
}
