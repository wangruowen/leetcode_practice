
public class RemoveDuplicatesfromSortedList {
	public ListNode deleteDuplicates(ListNode head) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ListNode root = new ListNode(-1);
        ListNode last = root, cur_node = head;
        while (cur_node != null) {
			ListNode next_node = cur_node.next;
			while (next_node != null && next_node.val == cur_node.val) {
				next_node = next_node.next;
			}
			last.next = cur_node;
			last = cur_node;
			last.next = null;
			cur_node = next_node;
		}
        return root.next;
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
