import java.util.ArrayList;
import java.util.Arrays;

public class Subsets { 
	public ArrayList<ArrayList<Integer>> subsets(int[] S) {
        Arrays.sort(S);
        return helper(S);
    }
	private ArrayList<ArrayList<Integer>> helper(int[] s) {
		ArrayList<ArrayList<Integer>> resultList = null;
		if (s.length == 0) {
			resultList = new ArrayList<ArrayList<Integer>>();
			resultList.add(new ArrayList<Integer>());
			return resultList;
		}
		int first = s[0];
		resultList = helper(Arrays.copyOfRange(s, 1, s.length));
		int size = resultList.size();
		for (int i = 0; i < size; i++) {
			ArrayList<Integer> newList = new ArrayList<Integer>(resultList.get(i));
			newList.add(0, first);
			resultList.add(newList);
		}
		return resultList;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Subsets().subsets(new int[] {1});
	}

}
