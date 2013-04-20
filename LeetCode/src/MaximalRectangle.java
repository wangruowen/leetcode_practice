public class MaximalRectangle {
	public int maximalRectangle(char[][] matrix) {
		if (matrix == null || matrix.length == 0) return 0;
        int[][] cnt = new int[matrix.length + 1][matrix[0].length + 1];
        
        int max = 0;
        for (int i = 1; i <= matrix.length; i++) {
			for (int j = 1; j <= matrix[i].length; j++) {
				if (matrix[i - 1][j - 1] == '1') {
					int up_val = cnt[i - 1][j];
					int left_val = cnt[i][j - 1];
					int left_up_val = cnt[i - 1][j - 1];
					if (up_val > 0 && left_val > 0 && left_up_val > 0) {
						cnt[i][j] = up_val + left_val - left_up_val + 1;
					} else {
						cnt[i][j] = 1;
					}
					
					max = Math.max(max, cnt[i][j]);
				}				
			}
		}
        
        return max;
    }

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
