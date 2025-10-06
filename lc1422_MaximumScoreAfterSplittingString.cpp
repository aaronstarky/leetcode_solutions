#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxScore(string s) {
        int *left = new int[s.length()];
        int *right = new int[s.length()];


        int currval = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '0') {
                currval++;
            }
            left[i] = currval;
        }


        currval = 0;
        for (int j = s.length()-1; j >= 0; j--) {
            if (s[j] == '1') {
                currval++;
            }
            right[j] = currval;
        }

        
        int max = 0;
        for (int i = 0; i < s.length()-1; i++) {
            if (left[i] + right[i+1] > max) {
                max = left[i] + right[i+1];
            }
        }
        return max;
    }
};

int main() {
    string input = "011101";
    Solution soln;
    int score = soln.maxScore(input);
    cout << "Max score: " << score << endl;
}

class Solution {
public:
    int maxScore(string s) {
        int *left = new int[s.length()];
        int *right = new int[s.length()];
        int currval = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '0') {
                currval++;
            }
            left[i] = currval;
        }
        currval = 0;
        for (int j = s.length()-1; j >= 0; j--) {
            if (s[j] == '1') {
                currval++;
            }
            right[j] = currval;
        }
        int max = 0;
        for (int i = 0; i < s.length()-1; i++) {
            if (left[i] + right[i+1] > max) {
                max = left[i] + right[i+1];
            }
        }
        return max;
    }
};