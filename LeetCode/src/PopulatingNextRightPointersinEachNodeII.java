public class PopulatingNextRightPointersinEachNodeII {
	public class TreeLinkNode {
		int val;
		TreeLinkNode left, right, next;

		TreeLinkNode(int x) {
			val = x;
		}
	}

	public void connect(TreeLinkNode most_left) {
		if (most_left == null)
			return;

		//BFS by using the next pointer
		TreeLinkNode next_parent = most_left;
		TreeLinkNode next_most_left = null;
		while (next_parent != null) {
			if (next_parent.left != null) {
				next_parent.left.next = findNextRight(next_parent, true);
				if (next_most_left == null) {
					next_most_left = next_parent.left;
				}
			}
			if (next_parent.right != null) {
				next_parent.right.next = findNextRight(next_parent, false);
				if (next_most_left == null) {
					next_most_left = next_parent.right;
				}
			}
			next_parent = next_parent.next;
		}

		connect(next_most_left);
	}

	private TreeLinkNode findNextRight(TreeLinkNode parent, boolean includeRight) {
		if (parent.right != null && includeRight) {
			return parent.right;
		} else {
			TreeLinkNode next_parent = parent.next;
			while (next_parent != null) {
				if (next_parent.left != null) {
					return next_parent.left;
				}
				if (next_parent.right != null) {
					return next_parent.right;
				}
				next_parent = next_parent.next;
			}
		}
		return null;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
