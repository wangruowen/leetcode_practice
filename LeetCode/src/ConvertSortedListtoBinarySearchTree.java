import java.util.ArrayList;
import java.util.List;

public class ConvertSortedListtoBinarySearchTree {
	public class ListNode {
		int val;
		ListNode next;

		ListNode(int x) {
			val = x;
			next = null;
		}
	}

	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;

		TreeNode(int x) {
			val = x;
		}
	}

	public TreeNode sortedListToBST(ListNode head) {
		// Transform the list to array
		ArrayList<ListNode> list = new ArrayList<ListNode>();
		ListNode node = head;
		while (node != null) {
			list.add(node);
			node = node.next;
		}
		
		return buildBST(list);
	}

	private TreeNode buildBST(List<ListNode> list) {
		int mid = (0 + list.size()) / 2;
		TreeNode node = new TreeNode(list.get(mid).val);
		if (mid > 1) {
			node.left = buildBST(list.subList(0, mid));
		} else {
			// mid == 1, there is only one node in the left side of mid
			node.left = new TreeNode(list.get(0).val);
		}
		if (mid + 2 < list.size()) {
			node.right = buildBST(list.subList(mid + 1, list.size()));
		} else {
			// there is only one node in the right hand side of mid
			node.right = new TreeNode(list.get(mid + 1).val);
		}		
		
		return node;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
