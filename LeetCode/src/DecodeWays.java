public class DecodeWays {
	public int numDecodings(String s) {
        if (s.length() == 0) {
    		return 0;
		}
        
    	int[] count = new int[s.length() + 1];
		count[0] = 1;
		for (int i = 0, j = 1; i < s.length(); i++, j++) {
			if (s.charAt(i) == '0') {
				if (i > 0 && (s.charAt(i - 1) == '1' || s.charAt(i - 1) == '2')) {
					count[j] = count[j - 2];
				} else {
					return 0;
				}
			} else if (i > 0
					&& (s.charAt(i - 1) == '1' || (s.charAt(i - 1) == '2' && s
							.charAt(i) <= '6'))) {
				count[j] = count[j - 2] + count[j - 1];
			} else {
				count[j] = count[j - 1];
			}
		}

		return count[s.length()];
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out
				.println(new DecodeWays()
						.numDecodings("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"));
	}

}
