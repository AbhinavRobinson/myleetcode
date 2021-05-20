// Given an integer array nums sorted in non-decreasing order,
// return an array of the squares of each number sorted in non-decreasing order.

// Runtime: 20 ms, faster than 97.93% of C++ online submissions for Squares of a Sorted Array.
// Memory Usage: 25.9 MB, less than 50.46% of C++ online submissions for Squares of a Sorted Array.

#include <math.h>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        vector<int> res(nums.size());
        int l = 0, r = nums.size() - 1;
        for (int k = nums.size() - 1; k >= 0; k--)
        {
            if (abs(nums[r]) > abs(nums[l]))
                res[k] = nums[r] * nums[r--];
            else
                res[k] = nums[l] * nums[l++];
        }
        return res;
    }
};