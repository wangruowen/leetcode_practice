public class BestTimeBuySellStock {
	public int maxProfit(int[] prices) {
		// Start typing your Java solution below
    	// DO NOT write main() function
		if (prices.length < 2)
    		return 0;
        
		int buy_date = 0;
		int max_profit = 0;
		
		for (int i = 0; i < prices.length; i++) {
			if (prices[i] < prices[buy_date]) {
				buy_date = i; 
			}
			int tmp_profit = prices[i] - prices[buy_date];
			if (tmp_profit > max_profit) max_profit = tmp_profit;
		}
		return max_profit;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
