public class AddTwoNum {
	private class ListNode {
		public int val;
		public ListNode next;

		public ListNode(int x) {
			val = x;
			next = null;
		}
	}

	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    	int carry = 0;
		ListNode rootListNode = new ListNode(-1);
		ListNode currentListNode = rootListNode;
		
		while (l1 != null || l2 != null) {
			int sum = carry;
			if (l1 != null) {
				sum += l1.val;
				l1 = l1.next;
			}
			if (l2 != null) {
				sum += l2.val;
				l2 = l2.next;
			}

			if (sum >= 10) {
				carry = 1;
				sum -= 10;
			} else {
    		    carry = 0;   
			}
			currentListNode.next = new ListNode(sum);
			currentListNode = currentListNode.next;
		}
        if (carry == 1) {
            currentListNode.next = new ListNode(carry);
        }

		return rootListNode.next;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
