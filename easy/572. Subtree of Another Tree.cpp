// Given the roots of two binary trees root and subRoot,
// return true if there is a subtree of root with the same structure and
// node values of subRoot and false otherwise.
// A subtree of a binary tree tree is a tree that consists of a node in tree
// and all of this node's descendants. The tree tree could also be
// considered as a subtree of itself.

// Runtime: 16 ms, faster than 95.72% of C++ online submissions
// for Subtree of Another Tree.
// Memory Usage: 28.7 MB, less than 93.85% of C++ online submissions
// for Subtree of Another Tree.

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
    bool isSubtree(TreeNode *root, TreeNode *subRoot)
    {
        if (root == nullptr) return false;
        if (hasSubRoot(root, subRoot)) return true;
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
    bool hasSubRoot(TreeNode *root, TreeNode *subRoot)
    {
        if (root == nullptr && subRoot == nullptr) return true;
        return root && subRoot && root->val == subRoot->val && hasSubRoot(root->left, subRoot->left) && hasSubRoot(root->right, subRoot->right);
    }
};