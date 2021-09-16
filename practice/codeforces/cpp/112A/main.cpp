#include <iostream>
#include <string>

using namespace std;

string make_lower(string in_string) {
	for(int i=0; i<in_string.length(); i++) {
		in_string[i] = tolower(in_string[i]);
	}
	return in_string;
}

int main() {
	string str1, str2;
	cin >> str1;
	cin >> str2;
	
	str1 = make_lower(str1);
	str2 = make_lower(str2);

	if(str1 > str2) {
		cout << 1;
	} else if(str1 < str2) {
		cout << -1;
	} else {
		cout << 0;
	}
}
