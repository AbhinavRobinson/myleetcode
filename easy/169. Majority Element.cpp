// Given an array nums of size n, return the majority element.
// The majority element is the element that appears more than
// ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
// Runtime: 12 ms, faster than 95.49% of C++ online submissions for Majority Element.
// Memory Usage: 19.5 MB, less than 80.87% of C++ online submissions for Majority Element.

// Boyer-Moore Majority Vote Algorithm

#include <vector>

using namespace std;

class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        int major = nums[0], count = 1;
        for (int i = 1; i < nums.size(); i++)
        {
            if (count == 0)
            {
                count++;
                major = nums[i];
            }
            else if (nums[i] == major)
                count++;
            else
                count--;
        }
        return major;
    }
};