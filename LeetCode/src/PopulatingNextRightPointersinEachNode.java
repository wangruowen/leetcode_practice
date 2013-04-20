
public class PopulatingNextRightPointersinEachNode {
	public class TreeLinkNode {
		int val;
		TreeLinkNode left, right, next;

		TreeLinkNode(int x) {
			val = x;
		}
	}

	public void connect(TreeLinkNode node) {
		if (node == null) return;
		
		if (node.left != null) {
			node.left.next = node.right;
		}
		if (node.right != null && node.next != null) {
			node.right.next = node.next.left;
		}
		// DFS
		connect(node.left);
		connect(node.right);
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
