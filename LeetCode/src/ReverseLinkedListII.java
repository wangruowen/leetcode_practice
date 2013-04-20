public class ReverseLinkedListII {
	public ListNode reverseBetween(ListNode head, int m, int n) {
    	int index = 0;
		ListNode root = new ListNode(0);
		root.next = head;
		ListNode cur_node = root;
		ListNode pre_m_node = root, m_node = root;
		while (index < m) {
			index++;
			if (index == m) {
				pre_m_node = cur_node;
				m_node = cur_node.next;
			}
			cur_node = cur_node.next;
		}

		index++;
		cur_node = m_node.next;
		while (index <= n) {
			m_node.next = cur_node.next;
			cur_node.next = pre_m_node.next;
			pre_m_node.next = cur_node;
			cur_node = m_node.next;
			index++;
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
