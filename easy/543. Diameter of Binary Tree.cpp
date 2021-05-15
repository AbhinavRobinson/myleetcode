// Given the root of a binary tree, return the length of the diameter of the tree.
// The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
// This path may or may not pass through the root.
// The length of a path between two nodes is represented by the number of edges between them.
//
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Diameter of Binary Tree.
// Memory Usage: 20.2 MB, less than 90.63% of C++ online submissions for Diameter of Binary Tree.

#include <algorithm>

struct TreeNode
{
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
  int ans = 0;
  int diameterOfBinaryTree(TreeNode *root)
  {
    this->getDiameter(root, 0);
    return this->ans;
  }
  int getDiameter(TreeNode *node, int diameter)
  {
    if (node != nullptr)
    {
      diameter++;
      int ldia = this->getDiameter(node->left, diameter);
      int rdia = this->getDiameter(node->right, diameter);
      this->ans = std::max(ans, ldia + rdia);
      return std::max(rdia, ldia) + 1;
    }
    return 0;
  }
};