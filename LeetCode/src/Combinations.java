import java.util.ArrayList;

public class Combinations {
	public ArrayList<ArrayList<Integer>> combine(int n, int k) {
		ArrayList<ArrayList<Integer>> tempList = new ArrayList<ArrayList<Integer>>();
		if (n == 0 || k == 0) {
			tempList.add(new ArrayList<Integer>());
			return tempList;
		} else {
			for (int i = 1; i <= n; i++) {
				ArrayList<Integer> newList = new ArrayList<Integer>();
				newList.add(i);
				tempList.add(newList);
			}
			if (k == 1) return tempList;
		}
		ArrayList<ArrayList<Integer>> resultList = null;
		for (int i = 1; i < k; i++) {
			resultList = new ArrayList<ArrayList<Integer>>();
			int size = tempList.size();
			for (int j = 0; j < size; j++) {
				ArrayList<Integer> oneList = tempList.get(j);
				int start = oneList.get(oneList.size() - 1) + 1;
				for (int l = start; l <= n; l++) {
					ArrayList<Integer> newList = new ArrayList<Integer>(oneList);
					newList.add(l);
					resultList.add(newList);
				}
			}
			if (i < k - 1) {
				tempList = resultList;
			}
		}

		return resultList;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(new Combinations().combine(1, 3));
	}

}
