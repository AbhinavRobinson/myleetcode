// Given an array of strings words representing an English Dictionary,
// return the longest word in words that can be built one character at a time by other words in words.
// If there is more than one possible answer, return the longest word
// with the smallest lexicographical order. If there is no answer, return the empty string.

// Runtime: 36 ms, faster than 92.80% of C++ online submissions for Longest Word in Dictionary.
// Memory Usage: 18.6 MB, less than 74.58% of C++ online submissions for Longest Word in Dictionary.

#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution
{
public:
    string longestWord(vector<string> &words)
    {
        sort(words.begin(), words.end());
        unordered_set<string> hash;
        string longest;
        for (string word : words)
        {
            if (word.length() == 1 || hash.count(word.substr(0, word.length() - 1)))
            {
                longest = word.length() > longest.length() ? word : longest;
                hash.insert(word);
            }
        }
        return longest;
    }
};