
public class SortColors {
	public void sortColors(int[] A) {
		if (A.length <= 1) {
			return;
		}
		
        int i = 0, j = A.length - 1;
        while (j >= 0 && A[j] == 2) {
			j--;
		}
        while (i < j) {        	
			if (A[i] == 2) {
				A[i] = A[j];
				A[j] = 2;
				j--;
				while (j >= 0 && A[j] == 2) {
					j--;
				}
			}
			i++;
		}
        i = 0; // reset i to 0
        while (j >= 0 && A[j] == 1) {
			j--;
		}
        while (i < j) {
			if (A[i] == 1) {
				A[i] = A[j];
				A[j] = 1;
				j--;
				while (j >= 0 && A[j] == 1) {
					j--;
				}
			}
			i++;
		}        
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
