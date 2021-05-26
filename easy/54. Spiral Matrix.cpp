// Given an m x n matrix, return all elements of the matrix in spiral order.
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Spiral Matrix.
// Memory Usage: 6.9 MB, less than 58.61% of C++ online submissions for Spiral Matrix.

#include <vector>;

using namespace std;

class Solution
{
public:
  vector<int> spiralOrder(vector<vector<int>> &matrix)
  {
    vector<int> res;
    vector<vector<int>> dir{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int nr = matrix.size();
    if (nr == 0)
      return res;
    int nc = matrix[0].size();
    if (nc == 0)
      return res;
    vector<int> size{nc, nr - 1};
    int iDir = 0;
    int ir = 0, ic = -1;
    while (size[iDir % 2])
    {
      for (int i = 0; i < size[iDir % 2]; ++i)
      {
        ir += dir[iDir][0];
        ic += dir[iDir][1];
        res.push_back(matrix[ir][ic]);
      }
      size[iDir % 2]--;
      iDir = (iDir + 1) % 4;
    }
    return res;
  }
};