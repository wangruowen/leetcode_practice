
public class SearchinRotatedSortedArrayII {
	public boolean search(int[] A, int target) {
		for (int i = 0; i < A.length; i++) {
			if (A[i] == target) {
				return true;
			}
		}
		return false;
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
