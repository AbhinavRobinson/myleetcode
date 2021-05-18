// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Two Sum.
// Memory Usage: 10.6 MB, less than 6.69% of C++ online submissions for Two Sum.

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
    
        for (int i = 0;; ++i) {
            auto it = hash.find(target - nums[i]);

            if (it != hash.end()) 
                return vector<int> {i, it->second};

            hash[nums[i]] = i;
        }
    }
};