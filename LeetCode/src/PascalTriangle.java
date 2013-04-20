import java.util.ArrayList;

public class PascalTriangle {
	public ArrayList<ArrayList<Integer>> generate(int numRows) {
		ArrayList<ArrayList<Integer>> resultList = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> one_row = new ArrayList<Integer>();
				
        if (numRows == 0) {
			return resultList;
		} else if (numRows == 1) {
			one_row.add(1);
			resultList.add(one_row);
			return resultList;
		} else {
			one_row.add(1);
			resultList.add(one_row);
			ArrayList<Integer> new_row = (ArrayList<Integer>) one_row.clone();
			new_row.add(1);
			resultList.add(new_row);
		}
        
        if (numRows == 2) {
			return resultList;
		}
        
        ArrayList<Integer> last_row = resultList.get(resultList.size() - 1);
        for (int i = 3; i <= numRows; i++) {        	
        	ArrayList<Integer> new_row = new ArrayList<Integer>();
        	
        	new_row.add(1);
        	for (int j = 0; j < last_row.size() - 1; j++) {
				new_row.add(last_row.get(j) + last_row.get(j + 1));
			}
        	new_row.add(1);
        	resultList.add(new_row);
        	last_row = new_row;
		}
        
        return resultList;
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(new PascalTriangle().generate(5));
	}

}
