#include <list>
#include <algorithm>
#include <iterator>
#include <iostream>

using namespace std;

int findCost(list<int> nums, int n) {
    int cost = 0;
    for (int i=1; i<n; i++) {
	//find index of i
	int j = std::distance(nums, std::find(nums, nums+n, i));
	cost += ((j+1)-i+1);
	//reversort
	std::reverse(std::next(nums.begin(), i-1),  std::next(nums.begin() , j));
	/*
	for(int l=0; l<(j-i)-1; l++) {
		int temp = nums[i-1+l];
		nums[i-1+l] = nums[j-l];
		nums[j-l] = temp;
	}
	*/
    }
    return cost;
}


int main() {
    int t;
    cin >> t;
    for (int k=0; k<t; k++){
        int cost = 0;
        int n; cin >> n;
	list<int> nums;
	//put all numbers into an array
	for (int j=0; j<n; j++) {
            int v; cin >> v;
	    nums[j] = v;
        }
	cost = findCost(nums, n);
        cout << "Case #" << k+1 << ": " << cost << endl;
    }
}
