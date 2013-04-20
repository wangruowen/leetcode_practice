public class BinaryTreeMaximumPathSum {

	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;

		TreeNode(int x) {
			val = x;
		}
	}

	public int maxPathSum(TreeNode root) {
		// max can be a single node val
		return maxPathSumWithSingles(root)[0];
	}

	private int[] maxPathSumWithSingles(TreeNode root) {
		int sum_of_singles = root.val;
		int max_of_all = sum_of_singles;
		int maxSingleLeft = sum_of_singles, maxSingleRight = sum_of_singles;
		
		if (root.left != null) {
			int[] maxLeft = maxPathSumWithSingles(root.left);
			
			if (maxLeft[0] > max_of_all)
				max_of_all = maxLeft[0];	
			if (maxLeft[1] > 0) {
				maxSingleLeft += maxLeft[1];
				sum_of_singles += maxLeft[1];
			}
		}
		if (root.right != null) {
			int[] maxRight = maxPathSumWithSingles(root.right);

			if (maxRight[0] > max_of_all)
				max_of_all = maxRight[0];	
			if (maxRight[1] > 0) {
				maxSingleRight += maxRight[1];
				sum_of_singles += maxRight[1];
			}
		}

		max_of_all = (max_of_all > sum_of_singles) ? max_of_all
				: sum_of_singles;
		int maxSingle = (maxSingleLeft > maxSingleRight) ? maxSingleLeft : maxSingleRight;

		return new int[] {max_of_all, maxSingle};
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
