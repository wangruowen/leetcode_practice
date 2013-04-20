public class MergeSortedArray {
	public void merge(int A[], int m, int B[], int n) {
		int i = m - 1, j = n - 1, k = A.length - 1;
		while (i >= 0 && j >= 0) {
			if (A[i] > B[j]) {
				A[k--] = A[i--];
			} else {
				A[k--] = B[j--];
			}
		}
		while (j >= 0) {
			A[j] = B[j];
			j--;
		}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] A = new int[] { 2 };
		int[] B = new int[] { 1 };
		new MergeSortedArray().merge(A, 1, B, 1);
		System.out.println(A);
	}

}
