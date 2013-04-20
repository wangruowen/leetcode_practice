import java.util.ArrayList;

public class SearchinRotatedSortedArray {
	public int search(int[] A, int target) {
		int start = 0;
		for (int i = 0; i < A.length - 1; i++) {
			if (A[i] > A[i + 1]) {
				start = i + 1;
				break;
			}
		}
		// recover the original array
		ArrayList<Integer> a_list = new ArrayList<Integer>();
		for (int i = start; i < A.length; i++) {
			a_list.add(A[i]);
		}
		for (int i = 0; i < start; i++) {
			a_list.add(A[i]);
		}
		int index = a_list.indexOf(target);
		if (index < 0) {
			return index;
		}
		return (index + start) % A.length;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
