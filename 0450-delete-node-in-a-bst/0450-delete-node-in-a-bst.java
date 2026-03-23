/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root == null) return null;
        if(root.val > key) root.left = deleteNode(root.left, key);
        else if(root.val < key) root.right = deleteNode(root.right, key);
        else{
            if(root.left == null) return root.right;
            else if(root.right == null) return root.left;
            else{
                if(root.right != null){
                    int x = minimum(root.right);
                    root.val = x;
                    root.right = deleteNode(root.right, x);
                }else{
                    int x = maximum(root.left);
                    root.val = x;
                    root.left = deleteNode(root.left, x);
                }
            }
        }
        return root;
    }

    static int minimum(TreeNode root){
        while(root.left != null){
            root = root.left ;
        }
        return root.val;
    }
    static int maximum(TreeNode root){
        while(root.right != null){
            root = root.right;
        }
        return root.val;
    }
}