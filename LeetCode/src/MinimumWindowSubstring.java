import java.util.ArrayList;
import java.util.HashMap;

public class MinimumWindowSubstring {
	private class CharInfo {
		char name;
		int index;

		public CharInfo(char name, int index) {
			this.name = name;
			this.index = index;
		}
	}

	public String minWindow(String S, String T) {
		ArrayList<CharInfo> char_list = new ArrayList<CharInfo>();
		HashMap<Character, ArrayList<CharInfo>> char_map = new HashMap<Character, ArrayList<CharInfo>>();
		HashMap<Character, Integer> char_count = new HashMap<Character, Integer>();
		for (int i = 0; i < T.length(); i++) {
			char one_char = T.charAt(i);
			int cnt = 1;
			if (char_count.containsKey(one_char)) {
				cnt += char_count.get(one_char);
			}
			char_count.put(one_char, cnt);
		}
		HashMap<Character, Integer> this_char_count = new HashMap<Character, Integer>();
		int window_size = Integer.MAX_VALUE, start = -1, end = -1;
		boolean isFull = false;
		for (int i = 0; i < S.length(); i++) {
			char cur_char = S.charAt(i);
			int index = T.indexOf(cur_char);
			if (index >= 0) {
				CharInfo new_char_info = new CharInfo(cur_char, i);
				if (char_map.containsKey(cur_char)) {
					ArrayList<CharInfo> cur_char_info_list = char_map
							.get(cur_char);
					if (cur_char_info_list.size() == char_count.get(cur_char)) {
						CharInfo old_char_info = cur_char_info_list.remove(0);
						char_list.remove(old_char_info);
					} else {
						int cnt = 1;
						if (this_char_count.containsKey(cur_char)) {
							cnt += this_char_count.get(cur_char);
						}
						this_char_count.put(cur_char, cnt);
					}
					cur_char_info_list.add(new_char_info);
				} else {
					ArrayList<CharInfo> new_char_info_list = new ArrayList<CharInfo>();
					new_char_info_list.add(new_char_info);
					char_map.put(cur_char, new_char_info_list);
					int cnt = 1;
					if (this_char_count.containsKey(cur_char)) {
						cnt += this_char_count.get(cur_char);
					}
					this_char_count.put(cur_char, cnt);
				}
				char_list.add(new_char_info);				

				if (!isFull) {
					boolean check = true;
					for (char char_name : char_count.keySet()) {
						if (!this_char_count.containsKey(char_name)
								|| char_count.get(char_name) != this_char_count
										.get(char_name)) {
							check = false;
							break;
						}
					}
					if (check) {
						isFull = true;
					}
				}
				
				if (isFull) {
					int tmp_start = char_list.get(0).index;
					int tmp_end = char_list.get(char_list.size() - 1).index;
					int tmp_size = tmp_end - tmp_start + 1;
					if (tmp_size < window_size) {
						window_size = tmp_size;
						start = tmp_start;
						end = tmp_end;
					}
				}
			}
		}
		if (start >= 0 && end >= 0)
			return S.substring(start, end + 1);
		else
			return "";
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println(new MinimumWindowSubstring().minWindow(
				"aa", "aa"));
	}

}
