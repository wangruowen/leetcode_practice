public class HammingWeight {
	// https://leetcode.com/problems/number-of-1-bits/
	public static int hammingWeight(int n) {
		int total_1_bit = 0;
		int bitmask = 0x0001;

		while (n != 0) {
			if ((n & bitmask) == bitmask) {
				total_1_bit++;
			}
			n = n >>> 1;
		}

		return total_1_bit;
	}

	public static void main(String[] args) {
		System.out.println(hammingWeight(11));
	}

}
