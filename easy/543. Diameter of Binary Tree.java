/**
 * Given the root of a binary tree, return the length of the diameter of the tree.
 * The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
 * This path may or may not pass through the root.
 * The length of a path between two nodes is represented by the number of edges between them.
 * 
 * 
 * Runtime: 0 ms, faster than 100.00% of Java online submissions for Diameter of Binary Tree.
 * Memory Usage: 40.4 MB, less than 5.02% of Java online submissions for Diameter of Binary Tree.
 */

/**
 * Definition for a binary tree node.
 */
class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode() {
  }

  TreeNode(int val) {
    this.val = val;
  }

  TreeNode(int val, TreeNode left, TreeNode right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

class Solution {
  int ans = 0;

  public int diameterOfBinaryTree(TreeNode root) {
    getDiameter(root, 0);
    return this.ans;
  }

  public int getDiameter(TreeNode node, int diameter) {
    if (node != null) {
      diameter++;
      if (node.left == null && node.right == null) {
        return 1;
      }
      int ldia = getDiameter(node.left, diameter);
      int rdia = getDiameter(node.right, diameter);
      this.ans = Math.max(ans, rdia + ldia);
      return Math.max(rdia, ldia) + 1;
    }
    return 0;
  }
}