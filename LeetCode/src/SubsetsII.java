import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class SubsetsII {
	public ArrayList<ArrayList<Integer>> subsetsWithDup(int[] num) {
		HashMap<String, ArrayList<Integer>> resultMap = new HashMap<String, ArrayList<Integer>>();
		resultMap.put("", new ArrayList<Integer>());
		if (num.length == 0) {
			return new ArrayList<ArrayList<Integer>>(resultMap.values());
		}
		Arrays.sort(num);
		getSubSets(num, resultMap);
		return new ArrayList<ArrayList<Integer>>(resultMap.values());
		
		// Another way
		Arrays.sort(num);
	    ArrayList<ArrayList<Integer>> ret = new ArrayList<ArrayList<Integer>>();
	    ret.add(new ArrayList<Integer>());

	    int start = 0;
	    for(int i = 0; i < num.length; i++)
	    {
	        int size = ret.size();
	        for(int j = start; j < size; j++)
	        {
	            ArrayList<Integer> sub = new ArrayList<Integer>(ret.get(j));
	            sub.add(num[i]);
	            ret.add(sub);
	        }
	        if(i < num.length - 1 && num[i + 1] == num[i])
	            start = size;
	        else
	            start = 0;
	    }

	    return ret;
	}

	private void getSubSets(int[] num,
			HashMap<String, ArrayList<Integer>> resultMap) {
		int first = num[0];
		if (num.length > 1) {
			getSubSets(Arrays.copyOfRange(num, 1, num.length), resultMap);
		}
				
		HashMap<String, ArrayList<Integer>> newMap = new HashMap<String, ArrayList<Integer>>();
		for (String int_str : resultMap.keySet()) {
			String new_str = Integer.toString(first) + "," + int_str;
			if (!resultMap.containsKey(new_str)) {
				ArrayList<Integer> new_list = new ArrayList<Integer>(resultMap.get(int_str));
				new_list.add(0, first);
				newMap.put(new_str, new_list);
			}
		}
		resultMap.putAll(newMap);
	}
	
	public static void main(String[] args) {
		System.out.println(new SubsetsII().subsetsWithDup(new int[]{1,2,2}));
	}
	
}
