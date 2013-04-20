public class FlattenBinaryTreetoLinkedList {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;

		TreeNode(int x) {
			val = x;
		}
	}

	public void flatten(TreeNode root) {
		flattenHelper(root);
	}

	private TreeNode flattenHelper(TreeNode node) {
		if (node == null)
			return null;
		// DFS
		TreeNode last_left = flattenHelper(node.left);
		TreeNode last_right = flattenHelper(node.right);

		if (last_left != null) {
			last_left.right = node.right;
			node.right = node.left;
			node.left = null;
		}
		// return the rightmost
		return last_right != null ? last_right : (last_left != null ? last_left
				: node);
	}
	
	private void another_flatten(TreeNode node) {
		if (node == null) {
			return;
		}
		
		TreeNode left = node.left;
		TreeNode right = node.right;
		
		node.right = left;
		node.left = null;
		
		// find the rightmost
		while (left.right != null) {
			left = left.right;
		}
		left.right = right;
		another_flatten(node.right);
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
