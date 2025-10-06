#include <iostream>
#include <string>
using namespace std;

const int I = 1;
const int V = 5;
const int X = 10;
const int L = 50;
const int C = 100;
const int D = 500;
const int M = 1000;

class Solution {
public:
   int romanToInt(string s) {
      bool atStart = false;
      int lastBiggest = s.length() - 1;
      int sum = 0;
      for (int i = s.length() - 1; i >= 0; i--) {
         if (GetValueOfCharacter(s[i]) > GetValueOfCharacter(s[lastBiggest])) {
            lastBiggest = i;
         }
         if (GetValueOfCharacter(s[i]) == GetValueOfCharacter(s[lastBiggest])) {
            sum += GetValueOfCharacter(s[i]);
         } else {
            sum -= GetValueOfCharacter(s[i]);
         }
      }
      return sum;
   }

private:
   int GetValueOfCharacter(char &c) {
      if (c == 'I') {
         return I;
      } else if (c == 'V') {
         return V;
      } else if (c == 'X') {
         return X;
      } else if (c == 'L') {
         return L;
      } else if (c == 'C') {
         return C;
      } else if (c == 'D') {
         return D;
      } else if (c == 'M') {
         return M;
      } else {
         return V;
      }
   }
};

int main() {
   string input = "MCMXCIV";
   Solution soln;
   int result = soln.romanToInt(input);
   cout << "Result is: " << result << endl;
   return 0;
}