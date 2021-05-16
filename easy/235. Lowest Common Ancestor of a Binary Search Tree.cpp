// Given a binary search tree (BST), find the lowest common ancestor (LCA)
// of two given nodes in the BST.
// According to the definition of LCA on Wikipedia: “The lowest common ancestor
// is defined between two nodes p and q as the lowest node in T that has both
// p and q as descendants (where we allow a node to be a descendant of itself).”

// Runtime: 20 ms, faster than 99.05% of C++ online submissions for Lowest Common Ancestor of a Binary Search Tree.
// Memory Usage: 23.1 MB, less than 76.95% of C++ online submissions for Lowest Common Ancestor of a Binary Search Tree.

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
  TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q)
  {
    if (p->val > q->val)
    {
      TreeNode *tmp = p;
      p = q;
      q = tmp;
    }
    while (true)
    {
      if ((root->val > p->val && root->val <= q->val) || (root->val >= p->val && root->val < q->val))
      {
        p = nullptr;
        q = nullptr;
        delete p;
        delete q;
        return root;
      }
      else
      {
        if (root->val > q->val)
          root = root->left;
        else
          root = root->right;
      }
    }
  }
};