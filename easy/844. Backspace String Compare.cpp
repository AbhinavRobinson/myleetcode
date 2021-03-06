// Given two strings s and t, return true if they are equal when both are
// typed into empty text editors. '#' means a backspace character.
// Note that after backspacing an empty text, the text will continue empty.

// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Backspace String Compare.
// Memory Usage: 6 MB, less than 92.75% of C++ online submissions for Backspace String Compare.

#include <string>

using namespace std;

class Solution
{
public:
    bool backspaceCompare(string s, string t)
    {
        int i = s.size() - 1, j = t.size() - 1, back;
        while (true)
        {
            back = 0;
            while (i >= 0 && (back > 0 || s[i] == '#'))
                back += s[i--] == '#' ? 1 : -1;
            back = 0;
            while (j >= 0 && (back > 0 || t[j] == '#'))
                back += t[j--] == '#' ? 1 : -1;

            if (i >= 0 && j >= 0 && s[i] == t[j])
            {
                i--;
                j--;
            }
            else
                break;
        }
        return i == -1 && j == -1;
    }
};