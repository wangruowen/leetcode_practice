public class AddBinary {
//	private static final int MAX_LENGTH = Integer.toBinaryString(
//			Integer.MAX_VALUE).length();
	
	private int cal_one_bit(int carry, int a_bit, int b_bit, StringBuilder stringBuilder) {
		int one_bit_sum = carry + a_bit + b_bit;
		if (one_bit_sum > 2) {
			carry = 1;
			stringBuilder.insert(0, '1');
		} else if (one_bit_sum == 2) {
			carry = 1;
			stringBuilder.insert(0, '0');
		} else if (one_bit_sum == 1) {
			carry = 0;
			stringBuilder.insert(0, '1');
		} else {
			carry = 0;
			stringBuilder.insert(0, '0');
		}
		
		return carry;
	}
	
	public String addBinary(String a, String b) {
		// find which one is longer, ensure a.length <= b.length
		if (a.length() > b.length()) {
			String tmp = a;
			a = b;
			b = tmp;
		}
		int carry = 0;
		int i = a.length() - 1, j = b.length() - 1;
		StringBuilder resultString = new StringBuilder();
		
		while (i >=0 && j >=0) {
			int a_one_bit = a.charAt(i) - '0';
			int b_one_bit = b.charAt(j) - '0';
			carry = cal_one_bit(carry, a_one_bit, b_one_bit, resultString);			
			i--;j--;
		}
		
		while (j >= 0) {
			int b_one_bit = b.charAt(j) - '0';
			carry = cal_one_bit(carry, 0, b_one_bit, resultString);	
			j--;			
		}
		
		if (carry == 1) {
			resultString.insert(0, '1');
		}
		return resultString.toString();
		
//		
//		if (a.length() < MAX_LENGTH && b.length() < MAX_LENGTH) {
//			return Integer.toBinaryString(Integer.parseInt(a, 2)
//					+ Integer.parseInt(b, 2));
//		} else {
//			return new BigInteger(a, 2).add(new BigInteger(
//					b, 2)).toString(2);
//		}
		
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(new AddBinary().addBinary("100", "110010"));
	}

}
