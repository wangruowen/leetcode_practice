import java.util.ArrayList;
import java.util.LinkedList;

public class BinaryTreeZigzagLevelOrderTraversal {
	public ArrayList<ArrayList<Integer>> zigzagLevelOrder(TreeNode root) {
    	ArrayList<ArrayList<Integer>> resultList = new ArrayList<ArrayList<Integer>>();
		if (root == null) {
			return resultList;
		}
		// Zigzag BFS
		boolean right_to_left = false;
		LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
		queue.offer(root);
		queue.offer(null); // null as delimiter
		
		ArrayList<Integer> one_layer_list = new ArrayList<Integer>();
		
		while (!queue.isEmpty()) {
			TreeNode node = queue.poll();
			if (node == null) {
				if (!one_layer_list.isEmpty()) {
					resultList.add(one_layer_list);
					one_layer_list = new ArrayList<Integer>();
					// toggle zigzag flag
					right_to_left = !right_to_left;
					queue.offer(null);
					continue;
				} else {
					break;
				}				
			}
			if (right_to_left) {
				one_layer_list.add(0, node.val);
			} else {
				one_layer_list.add(node.val);
			}

			if (node.left != null) {
				queue.offer(node.left);
			}
			if (node.right != null) {
				queue.offer(node.right);
			}
		}
		
        return resultList;
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
