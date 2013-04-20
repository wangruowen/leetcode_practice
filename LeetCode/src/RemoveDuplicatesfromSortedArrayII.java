public class RemoveDuplicatesfromSortedArrayII {
	public int removeDuplicates(int[] A) {
        if (A.length < 2) return A.length;

		int k = 2;
		for (int i = 2; i < A.length; i++) {
			if (!(A[k - 2] == A[k - 1] && A[k - 1] == A[i])) {
				A[k++] = A[i];
			}
		}

		return k;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] A= new int[] { 1, 1, 1, 2, 2, 3 };
		System.out.println(new RemoveDuplicatesfromSortedArrayII()
				.removeDuplicates(A));
		for (int i : A) {
			System.out.print(i + " ");
		}
	}

}
