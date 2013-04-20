
public class SymmetricTree {
	public boolean isSymmetric(TreeNode root) {
		if (root == null) return true;
        return isSymmetricHelper(root.left, root.right);
    }
	
	private boolean isSymmetricHelper(TreeNode left, TreeNode right) {
		if (left == null && right == null) {
			return true;
		} else if (left == null || right == null) {
			return false;
		} else {
			if (left.val == right.val) {
				return isSymmetricHelper(left.left, right.right) && isSymmetricHelper(left.right, right.left);
			}
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
