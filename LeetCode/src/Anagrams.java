import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class Anagrams {

	private String getCharBitMap(String str) {
		char[] char_array = str.toCharArray();
		int[] char_cnt = new int[26];
		for (char c : char_array) {
			char_cnt[c - 'a'] += 1;
		}
		// create a string to represent the bitmap, later the string is used as key in the hashmap
		return Arrays.toString(char_cnt);
	}
	
	public ArrayList<String> anagrams(String[] strs) {
		HashMap<String, ArrayList<String>> anaHashMap = new HashMap<String, ArrayList<String>>();
        // Start typing your Java solution below
        // DO NOT write main() function
        for (String string : strs) {
        	String charBitMap = getCharBitMap(string);
        	if (anaHashMap.containsKey(charBitMap)) {
        		anaHashMap.get(charBitMap).add(string);
        	} else {
        		ArrayList<String> newArrayList = new ArrayList<String>();
        		newArrayList.add(string);
        		anaHashMap.put(charBitMap, newArrayList);
        	}
			
		}
        ArrayList<String> resultList = new ArrayList<String>();
        for (ArrayList<String> strList : anaHashMap.values()) {
        	if (strList.size() > 1) {
        		resultList.addAll(strList);
        	}			
		}
        return resultList;
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Anagrams oneAnagrams = new Anagrams();
		System.out.println(oneAnagrams.anagrams(new String[]{"c", "c"}));
	}

}
