import java.util.ArrayList;

public class BinaryTreeLevelOrderTraversalII {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;

		TreeNode(int x) {
			val = x;
		}
	}

	private ArrayList<ArrayList<Integer>> resultList;

	public ArrayList<ArrayList<Integer>> levelOrderBottom(TreeNode root) {
		resultList = new ArrayList<ArrayList<Integer>>();
		if (root == null)
			return resultList;

		ArrayList<TreeNode> root_list = new ArrayList<TreeNode>();
		root_list.add(root);
		getNextLevelNodes(root_list);

		return resultList;
	}

	private void getNextLevelNodes(ArrayList<TreeNode> parent_list) {
		ArrayList<TreeNode> children_list = new ArrayList<TreeNode>();
		ArrayList<Integer> parent_vals = new ArrayList<Integer>();

		for (TreeNode parent : parent_list) {
			if (parent.left != null)
				children_list.add(parent.left);
			if (parent.right != null)
				children_list.add(parent.right);
			parent_vals.add(parent.val);
		}
		resultList.add(0, parent_vals);
		if (!children_list.isEmpty()) {
			// BFS
			getNextLevelNodes(children_list);
		}

	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
