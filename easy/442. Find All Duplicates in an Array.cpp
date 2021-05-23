// Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
// You must write an algorithm that runs in O(n) time and uses only constant extra space.

// Runtime: 48 ms, faster than 80.36% of C++ online submissions for Find All Duplicates in an Array.
// Memory Usage: 33.5 MB, less than 90.71% of C++ online submissions for Find All Duplicates in an Array.

#include <math.h>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> findDuplicates(vector<int> &nums)
    {
        vector<int> results;
        for (int i = 0; i < nums.size(); i++)
        {
            int index = abs(nums[i]) - 1;
            nums[index] *= -1;
            if (nums[index] > 0)
            {
                if (results.size() == 0 || results[results.size() - 1] != nums[i]) results.push_back(abs(nums[i]));
            }
        }
        return results;
    }
};