// Given the root of a binary tree, return its maximum depth.
// A binary tree's maximum depth is the number of nodes along
// the longest path from the root node down to the farthest leaf node.
//
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for
// Maximum Depth of Binary Tree.
// Memory Usage: 18.8 MB, less than 87.53% of C++ online submissions for
// Maximum Depth of Binary Tree.

/**
 * Definition for a binary tree node.
 */

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
  // recursive DFS
  int maxDepth(TreeNode *root)
  {
    if (!root)
      return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
  }

  // non recursive BFS
  int maxDepth_non_recursive(TreeNode *root)
  {
    if (root == nullptr)
      return 0;
    deque<tuple<TreeNode *, int>> queue;
    queue.push_back(make_tuple(root, 1));
    int max_level = 1;
    while (!queue.empty())
    {
      tuple<TreeNode *, int> elem = queue.front();
      queue.pop_front();
      TreeNode *node = get<0>(elem);
      int level = get<1>(elem);
      if (node != nullptr)
      {
        if (level > max_level)
          max_level = level;
        queue.push_back(make_tuple(node->left, level + 1));
        queue.push_back(make_tuple(node->right, level + 1));
      }
    }
    return max_level;
  }
};