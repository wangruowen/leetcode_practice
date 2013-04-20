import java.util.Arrays;

public class Searcha2DMatrix {
	public boolean searchMatrix(int[][] matrix, int target) {
		int[] first_int_array = new int[matrix.length];
		for (int i = 0; i < matrix.length; i++) {
			first_int_array[i] = matrix[i][0];
		}
		int row_num = myBinarySearch(matrix, 0,
				first_int_array.length, target);
		int result = Arrays.binarySearch(matrix[row_num], target);
		return result >= 0 ? true : false;
	}

	private int myBinarySearch(int[][] matrix, int start, int end, int target) {
		int mid = (start + end) / 2;
		if (mid == start) {
			return mid;
		}

		if (matrix[mid][0] <= target) {
			return myBinarySearch(matrix, mid, end, target);
		} else {
			return myBinarySearch(matrix, start, mid, target);
		}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Searcha2DMatrix().searchMatrix(new int[][] { { 1 } }, 0);
	}

}
