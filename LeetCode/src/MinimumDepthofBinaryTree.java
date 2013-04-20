import java.util.LinkedList;
import java.util.Queue;

public class MinimumDepthofBinaryTree {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;

		TreeNode(int x) {
			val = x;
		}
	}

	public int minDepth(TreeNode root) {
		if (root == null) return 0;
		
		root.val = 1;
		LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
		queue.offer(root);

		int min = 0;
		while (!queue.isEmpty()) {
			TreeNode node = queue.poll();
			if (node.left == null && node.right == null) {
				// reach the first leaf
				min = node.val;
				break;
			} else {
				// BFS
				if (node.left != null) {
					node.left.val = node.val + 1;
					queue.add(node.left);
				}
				if (node.right != null) {
					node.right.val = node.val + 1;
					queue.add(node.right);
				}
			}
		}

		return min;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
