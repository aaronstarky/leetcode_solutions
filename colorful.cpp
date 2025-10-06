#include <iostream>
#include <string>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        vector<char> cols;
        for (char color : colors) {
            cols.push_back(color);
        }
        cols.in
        int cost = 0;
        for (int i = 0; i < cols.size()-1; i++) {
            if (cols[i] == cols[i+1]) {
                if (neededTime[i] <= neededTime[i+1]) {
                    cost += neededTime[i];
                    neededTime.erase(neededTime.begin() + i); // Removes the element at index i from vector vec
                    cols.erase(cols.begin() + i);
                    i--;
                } else {
                    cost += neededTime[i+1];
                    neededTime.erase(neededTime.begin() + i + 1); // Removes the element at index i from vector vec
                    cols.erase(cols.begin() + i + 1);
                }
            }
        }
        return cost;
    }
};

int main() {
    Solution soln;
    string colors = "aabaa";
    vector<int> nt{1,2,3,4,1};
    int result = soln.minCost(colors, nt);
    cout << "Minimum cost: " << result << endl;
    return 0;
}
