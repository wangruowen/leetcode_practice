import java.util.HashMap;

public class EditDistance {
	private HashMap<String, Integer> edit_memo = null;
    public int minDistance(String word1, String word2) {
        edit_memo = new HashMap<String, Integer>();
		return helper(word1, 0, word2, 0);
	}

	private int helper(String word1, int i, String word2, int j) {	
        String key = Integer.toString(i) + "," + Integer.toString(j);
    	if (edit_memo.containsKey(key)) {
			return edit_memo.get(key);
		}
        
		int edit = 0;
		if (j == word2.length() && i < word1.length()) {
			edit = word1.length() - i;
		} else if (i == word1.length() && j < word2.length()) {
			edit = word2.length() - j;
		} else if (i < word1.length() && j < word2.length()) {
			if (word1.charAt(i) == word2.charAt(j)) {
				edit = helper(word1, i + 1, word2, j + 1);
			} else {
				// insert
				int if_insert = helper(word1, i, word2, j + 1) + 1;
				// replace
				int if_replace = helper(word1, i + 1, word2, j + 1) + 1;
				// delete
    			int if_delete = helper(word1, i + 1, word2, j) + 1;
				edit = Math.min(if_delete, Math.min(if_insert, if_replace));
			}
		}

        edit_memo.put(key, edit);
		return edit;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(new EditDistance().minDistance("sea", "eat"));
	}

}
