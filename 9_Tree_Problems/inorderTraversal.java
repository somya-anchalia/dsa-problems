// https://takeuforward.org/data-structure/inorder-traversal-of-binary-tree/

// https://leetcode.com/problems/binary-tree-inorder-traversal/


import java.util.*;


// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public ArrayList<Integer> list;
    public void fun(TreeNode root){
        if(root == null){
            return ;
        }
        fun(root.left);
        list.add(root.val);
        fun(root.right);
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        list = new ArrayList<>();
        fun(root);
        return list;
    }
}

public class inorderTraversal {
    public static void main(String args[]) {
        TreeNode root= new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        // Getting inorder traversal
        List<Integer> result = new Solution().inorderTraversal(root);

        // Displaying the inorder traversal result
        System.out.print("Inorder Traversal: ");
        // Output each value in the
        // inorder traversal result
        for (int val : result) {
            System.out.print(val + " ");
        }
        System.out.println();
    }
}

//   1
//  2 3
// 4 5