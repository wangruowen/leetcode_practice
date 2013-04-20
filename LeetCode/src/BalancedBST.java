public class BalancedBST {
	private class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;

		TreeNode(int x) {
			val = x;
		}
	}
	private static final int NOT_BALANCED = -1;
	
	private int getDepthWithBalanceCheck(TreeNode node) {
		int depth = 0;
		
		if (node != null) {
			int left_depth = getDepthWithBalanceCheck(node.left);
			int right_depth = getDepthWithBalanceCheck(node.right);
			
			if (left_depth == NOT_BALANCED || right_depth == NOT_BALANCED) {
				depth = NOT_BALANCED;
			} else {
				int depth_diff = left_depth - right_depth;
				if (Math.abs(depth_diff) > 1) {
					depth = NOT_BALANCED;
				} else {
					depth = (left_depth > right_depth ? left_depth : right_depth) + 1;
				}
			}			
		}
		
		return depth;
	}
	
	public boolean isBalanced(TreeNode root) {
		if (root == null) return true;
		
		if (getDepthWithBalanceCheck(root) != NOT_BALANCED) {
			return true;
		} else {
			return false;
		}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
