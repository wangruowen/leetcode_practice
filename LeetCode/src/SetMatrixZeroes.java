
public class SetMatrixZeroes {
	public void setZeroes(int[][] matrix) {
		// use the first row and column as marker to zerofy the rest matrix first
		// then come back to see if the first row and column need to be zerofy.
		boolean firstRowHasZero = false, firstColHasZero = false;
		int row_size = matrix.length, col_size = matrix[0].length;
		for (int i = 0; i < row_size; i++) {
			if (matrix[i][0] == 0) {
				firstColHasZero = true;
				break;
			}
		}
		for (int j = 0; j < col_size; j++) {
			if (matrix[0][j] == 0) {
				firstRowHasZero = true;
				break;
			}
		}
		
		for (int i = 1; i < row_size; i++) {
			for (int j = 1; j < col_size; j++) {
				if (matrix[i][j] == 0) {
					matrix[0][j] = 0;
					matrix[i][0] = 0;
				}
			}
		}
		
		for (int i = 1; i < row_size; i++) {
			if (matrix[i][0] == 0) {
				for (int j = 1; j < col_size; j++) {
					matrix[i][j] = 0;
				}
			}
		}
		
		for (int j = 1; j < col_size; j++) {
			if (matrix[0][j] == 0) {
				for (int i = 1; i < row_size; i++) {
					matrix[i][j] = 0;
				}
			}
		}
		
		if (firstColHasZero) {
			for (int i = 0; i < row_size; i++) {
				matrix[i][0] = 0;
			}
		}
		
        if (firstRowHasZero) {
			for (int j = 0; j < col_size; j++) {
				matrix[0][j] = 0;
			}
		}
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
