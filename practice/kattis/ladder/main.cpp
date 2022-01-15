#include <iostream>
#include <math.h>

#define PI 3.14159265

using namespace std;

int main() {
	double h, v, x;
	cin >> h >> v;
	x = ceil(h / sin(v*PI/180));
	cout << x << endl;
}
