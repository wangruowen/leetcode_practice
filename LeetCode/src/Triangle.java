import java.util.ArrayList;

public class Triangle {
	// For tree-like sum/path problem, we can think about bottom-up instead of top-down
	public int minimumTotal(ArrayList<ArrayList<Integer>> triangle) {
		for (int i = triangle.size() - 2; i >= 0; i--) {
			ArrayList<Integer> cur_layer = triangle.get(i);
			ArrayList<Integer> child_layer = triangle.get(i + 1);
			for (int j = 0; j < cur_layer.size(); j++) {
				int origin_val = cur_layer.get(j);
				cur_layer.set(j, origin_val + Math.min(child_layer.get(j), child_layer.get(j + 1)));
			}
		}
		return triangle.get(0).get(0);
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
