public class ReverseBit {
	// you need treat n as an unsigned value
	public static int reverseBits(int n) {
		int r = 0;
		for (int i = 0; i < 32; i++) {
			r >>>= 1;
			r += (n & 0x80000000);
			n <<= 1;
		}

		return r;
	}

	public static void main(String[] args) {
		System.out.println(reverseBits(43261596));
	}

	private static String convertIntToBit(int n) {
		StringBuilder sb = new StringBuilder();

		boolean opposite = false;
		if (n < 0) {
			opposite = true;
			n = ~n;
		}

		for (int i = 0; i < 32; i++) {
			if ((n & 1) == 1) {
				if (opposite) {
					sb.append("0");
				} else {
					sb.append("1");
				}
			} else {
				if (opposite) {
					sb.append("1");
				} else {
					sb.append("0");
				}
			}
			n >>>= 1;
		}

		return sb.reverse().toString();
	}
}
