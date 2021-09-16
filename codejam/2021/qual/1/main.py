#include <iostream>
#include <algorithm>
"""
using namespace std;

int findCost(int nums[], int n) {
    int cost = 0;
    for (int i=1; i<n; i++) {
        //find index of i
        int j = std::distance(nums, std::find(nums, nums+n, i));
        cost += ((j+1)-i+1);
        //reversort
        for(int l=0; l<(j-i)-1; l++) {
                int temp = nums[i-1+l];
                nums[i-1+l] = nums[j-l];
                nums[j-l] = temp;
        }
    }
    return cost;
}
"""
import sys

def findCost(inarr):
    cost = 0
    for i in range(len(inarr)-1):
        print(i)

t = int(input()) 
for k in range(t):
    cost = 0
    n = sys.stdin
    myarr = (input().split())
    print(f"Case #{k+1}: {findCost(myarr)}")
