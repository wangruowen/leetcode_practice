public class ScrambleString {
	public boolean isScramble(String s1, String s2) {
		// find the position of first char in s2
		int fc_index = s2.indexOf(s1.charAt(0));
		if (fc_index < 0)
			return false;
		boolean left_sub = true, right_sub = true;
		if (fc_index < s2.length() - 1) {
			right_sub = isScramble(s1.substring(fc_index + 1, s1.length()),
					s2.substring(fc_index + 1, s2.length()));
		}
		if (fc_index > 0) {
			left_sub = isScramble(s1.substring(1, fc_index + 1),
					s2.substring(0, fc_index));
		}
		if (left_sub && right_sub) {
			return true;
		} else {
			boolean left_sub2 = true, right_sub2 = true;
			if (fc_index < s2.length() - 1) {
				right_sub2 = isScramble(s1.substring(1, s1.length() - fc_index),
						s2.substring(fc_index + 1, s2.length()));
			}
			if (fc_index > 0) {
				left_sub2 = isScramble(s1.substring(s1.length() - fc_index, s1.length()),
						s2.substring(0, fc_index));
			}
			return left_sub2 && right_sub2;
		}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(new ScrambleString().isScramble("a", "a"));
	}

}
