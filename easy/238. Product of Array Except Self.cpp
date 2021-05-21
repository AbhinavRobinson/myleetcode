// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
// You must write an algorithm that runs in O(n) time and without using the division operation.

// Runtime: 24 ms, faster than 51.60% of C++ online submissions for Product of Array Except Self.
// Memory Usage: 24 MB, less than 76.16% of C++ online submissions for Product of Array Except Self.

#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        int size = nums.size();
        int l = 1;
        int r = 1;
        vector<int> result(size, 1);
        for (int i = 0; i < size; i++)
        {
            result[i] *= l;
            l *= nums[i];
            result[size - 1 - i] *= r;
            r *= nums[size - 1 - i];
        }
        return result;
    }
};