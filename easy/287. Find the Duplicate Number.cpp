// Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
// There is only one repeated number in nums, return this repeated number.
// You must solve the problem without modifying the array nums and uses only constant extra space.

// Runtime: 92 ms, faster than 46.66% of C++ online submissions for Find the Duplicate Number.
// Memory Usage: 61.2 MB, less than 30.39% of C++ online submissions for Find the Duplicate Number.

#include <vector>

using namespace std;

class Solution
{
public:
    int findDuplicate(vector<int> &nums)
    {
        for (int i = 0; i < nums.size(); i++)
        {
            nums[abs(nums[i]) - 1] *= -1;
            if (nums[abs(nums[i]) - 1] > 0) return abs(nums[i]);
        }
        return -1;
    }
};