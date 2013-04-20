import java.util.LinkedList;

public class MaximumDepthofBinaryTree {
	
	public int maxDepth(TreeNode root) {		
		if (root == null) {
			return 0;
		} else {
			root.val = 1;
		}
        //BFS
		LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
		queue.offer(root);
		TreeNode node = null;
		while (!queue.isEmpty()) {
			node = queue.poll();
			
			if (node.left != null) {
				node.left.val = node.val + 1;
				queue.offer(node.left);
			}
			if (node.right != null) {
				node.right.val = node.val + 1;
				queue.offer(node.right);
			}
		}
        return node.val;
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
