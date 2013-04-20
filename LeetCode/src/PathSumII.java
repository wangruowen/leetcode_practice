import java.util.ArrayList;

public class PathSumII {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;

		TreeNode(int x) {
			val = x;
		}
	}

	public ArrayList<ArrayList<Integer>> pathSum(TreeNode node, int sum) {
		ArrayList<ArrayList<Integer>> resultList = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> path_list = new ArrayList<Integer>();
		pathSumHelper(node, sum, path_list, resultList);

		return resultList;
	}

	private void pathSumHelper(TreeNode node, int sum,
			ArrayList<Integer> path_list,
			ArrayList<ArrayList<Integer>> resultList) {
		if (node == null)
			return;

		int new_sum = sum - node.val;
		path_list.add(node.val);

		// When encounter leaf, check val with new_sum
		if (node.left == null && node.right == null && new_sum == 0) {
			resultList.add(path_list);
		}

		if (node.left != null) {
			ArrayList<Integer> left_path_list = new ArrayList<Integer>(
					path_list);
			pathSumHelper(node.left, new_sum, left_path_list, resultList);
		}
		if (node.right != null) {
			ArrayList<Integer> right_path_list = new ArrayList<Integer>(
					path_list);
			pathSumHelper(node.right, new_sum, right_path_list, resultList);
		}
	}

	public boolean hasPathSum(TreeNode node, int sum) {
		// Start typing your Java solution below
		// DO NOT write main() function
		if (node == null) return false;

		int new_sum = sum - node.val;

		// When encounter leaf, check val with new_sum
		if (node.left == null && node.right == null && new_sum == 0) {
			return true;
		}

		if (node.left != null && hasPathSum(node.left, new_sum)) {
			return true;
		} else if (node.right != null && hasPathSum(node.right, new_sum)) {
			return true;
		}
		return false;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
