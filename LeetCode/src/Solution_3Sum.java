import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Set;
import java.util.TreeSet;

public class Solution_3Sum {
	public ArrayList<ArrayList<Integer>> threeSum(int[] num) {
		ArrayList<ArrayList<Integer>> resultList = new ArrayList<ArrayList<Integer>>();
		Arrays.sort(num);
		for (int i = 0; i < num.length - 2; i++) {
			if (i > 0 && num[i] == num[i - 1]) continue;
			int j = i + 1;
			int k = num.length - 1;
			while (j < k) {
				int three_sum = num[i] + num[j] + num[k];
				if (three_sum > 0) {
					k--;
				} else if (three_sum < 0) {
					j++;
				} else {
					Integer[] tmp = { num[i], num[j], num[k] };
					resultList.add(new ArrayList<Integer>(Arrays.asList(tmp)));
					j++;
					k--;
				}
			}
		}
		return removeDuplicates(resultList);
	}

	public ArrayList<ArrayList<Integer>> removeDuplicates(ArrayList<ArrayList<Integer>> list) {
		Set<ArrayList<Integer>> set = new TreeSet<ArrayList<Integer>>(
				new Comparator<ArrayList<Integer>>() {
					@Override
					public int compare(ArrayList<Integer> o1,
							ArrayList<Integer> o2) {
						if (o1.equals(o2)) {
							return 0;
						} else {
							return 1;
						}
					}
				});
		set.addAll(list);
		return new ArrayList<ArrayList<Integer>>(set);
	}

	public static void main(String[] args) {
		Solution_3Sum solution = new Solution_3Sum();
		ArrayList<ArrayList<Integer>> list = solution.threeSum(new int[] { -1,
				0, 1, 2, -1, -4 });
		System.out.println(list);
	}
}
