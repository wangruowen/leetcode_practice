import java.util.Arrays;

public class Solution_3Sum_Closest {

	public int threeSumClosest(int[] num, int target) {
    	Arrays.sort(num);
		int min = Integer.MAX_VALUE;
		int sum = 0;
		for (int i = 0; i < num.length - 2; i++) {
			int j = i + 1;
			int k = num.length - 1;
			while (j < k) {
				int tmp_sum = num[i] + num[j] + num[k];
				int diff = tmp_sum - target;
				if (Math.abs(diff) >= min) {
					if (diff > 0) {
						k--;
					} else {
						j++;
					}
				} else {
					min = Math.abs(diff);
					sum = tmp_sum;
					if (diff > 0) {
    					k--;
					} else {
						j++;
					}
				}
			}
		}
        
		return sum;
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
