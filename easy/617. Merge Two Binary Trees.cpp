// You are given two binary trees root1 and root2.
// Imagine that when you put one of them to cover the other,
// some nodes of the two trees are overlapped while the others are not.
// You need to merge the two trees into a new binary tree.
// The merge rule is that if two nodes overlap, then sum node
// values up as the new value of the merged node. Otherwise,
// the NOT null node will be used as the node of the new tree.
// Return the merged tree.
// Note: The merging process must start from the root nodes of both trees.
//
// Runtime: 32 ms, faster than 81.90% of C++ online submissions for Merge Two Binary Trees.
// Memory Usage: 32.9 MB, less than 21.67% of C++ online submissions for Merge Two Binary Trees.

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
  TreeNode *mergeTrees(TreeNode *root1, TreeNode *root2)
  {
    TreeNode *newRoot = this->merger(root1, root2);
    delete root1;
    delete root2;
    return newRoot;
  }

  TreeNode *merger(TreeNode *node1, TreeNode *node2)
  {
    TreeNode *node = nullptr;
    if (node1 != nullptr && node2 != nullptr)
    {
      node = new TreeNode(node1->val + node2->val);
      node->left = this->merger(node1->left, node2->left);
      node->right = this->merger(node1->right, node2->right);
    }
    else
    {
      if (node1 != nullptr)
      {
        node = new TreeNode(node1->val, node1->left, node1->right);
      }
      else if (node2 != nullptr)
      {
        node = new TreeNode(node2->val, node2->left, node2->right);
      }
    }
    return node;
  }
};