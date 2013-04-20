import java.util.ArrayList;

public class RestoreIPAddresses {
	public ArrayList<String> restoreIpAddresses(String s) {
		return getRestIPNums(s, 4);
	}

	private ArrayList<String> getRestIPNums(String s, int num_of_parts) {
		ArrayList<String> resultList = new ArrayList<String>();
		boolean found = false;

		if (num_of_parts == 1) {
			if (isValidIPNum(s)) {
				found = true;
				resultList.add(s);
			}
		} else {
			for (int first_part = 1; first_part <= Math.min(4, s.length()); first_part++) {
				String first_str = s.substring(0, first_part);
				if (isValidIPNum(first_str)) {
					ArrayList<String> restList = getRestIPNums(
							s.substring(first_part, s.length()),
							num_of_parts - 1);
					if (restList != null) {
						for (String rest_part : restList) {
							found = true;
							resultList.add(first_str + "." + rest_part);
						}
					}
				}
			}
		}
		if (num_of_parts == 4) {
			return resultList;
		} else {
			return found ? resultList : null;
		}
	}

	private boolean isValidIPNum(String num_str) {
		if (num_str.length() > 0 && num_str.length() < 4) {
			if (!num_str.startsWith("0") || num_str.length() == 1) {
				int num = Integer.parseInt(num_str);
				if (num >= 0 && num <= 255) {
					return true;
				}
			}
		}
		return false;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(new RestoreIPAddresses().restoreIpAddresses("0279245587303"));
	}

}
