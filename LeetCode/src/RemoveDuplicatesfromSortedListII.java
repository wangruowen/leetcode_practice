
public class RemoveDuplicatesfromSortedListII {
	public ListNode deleteDuplicates(ListNode head) {
    	if (head == null) return null;
		
        ListNode root = new ListNode(-1);
        ListNode root_last = root, cur_node = head;
        while (cur_node != null) {
			ListNode next_node = cur_node.next;
			boolean found_dup = false;
			while (next_node != null && next_node.val == cur_node.val) {
				found_dup = true;				
				next_node = next_node.next;
			}
			if (found_dup) {
				// skip cur_node, directly to next_node
				cur_node = next_node;
			} else {
				root_last.next = cur_node;
				root_last = cur_node;
				root_last.next = null;// clear the original next
				cur_node = next_node;
			}
		}
        return root.next;
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ListNode head = new ListNode(1);
		head.next = new ListNode(2);
		head.next.next = new ListNode(2);
		new RemoveDuplicatesfromSortedListII().deleteDuplicates(head);
	}

}
