public class RotateArray {
	public static void rotate(int[] nums, int k) {
		k = k % nums.length;
		int[] tmp_holder = new int[k];
		for (int i = nums.length - k; i < nums.length; i++) {
			tmp_holder[i - (nums.length - k)] = nums[i];
		}
		for (int i = nums.length - k - 1; i >= 0; i--) {
			nums[i + k] = nums[i];
		}
		for (int i = 0; i < k; i++) {
			nums[i] = tmp_holder[i];
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
