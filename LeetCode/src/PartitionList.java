public class PartitionList {
	public ListNode partition(ListNode head, int x) {
		ListNode root = new ListNode(-1);
		ListNode pivot = new ListNode(x);
		ListNode root_last = root, pivot_last = pivot;

		ListNode cur_node = head;
		while (cur_node != null) {
			ListNode next = cur_node.next;
			if (cur_node.val < x) {
				root_last.next = cur_node;
				root_last = cur_node;
			} else {
				pivot_last.next = cur_node;
				pivot_last = cur_node;
				pivot_last.next = null;
			}
			cur_node = next;
		}
		root_last.next = pivot.next;

		return root.next;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ListNode head = new ListNode(2);
		head.next = new ListNode(1);
		ListNode result = new PartitionList().partition(head, 2);
		while (result != null) {
			System.out.println(result.val);
			result = result.next;
		}
		
	}

}
