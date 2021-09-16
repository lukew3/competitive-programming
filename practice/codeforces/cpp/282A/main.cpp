#include <iostream>
#include <string>

using namespace std;

int main() {
	int n;
	int value = 0;
	string temp_string;
	cin >> n;
	for(int i = 0; i < n; i++) {
		cin >> temp_string;
		if(temp_string[1] == '+') {
			value++;
		} else if(temp_string[1] == '-') {
			value--;
		}
	}
	cout << value;
}
