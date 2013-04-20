
public class BestTimeBuySellStockII {
	public int maxProfit(int[] prices) {
		if (prices.length < 2) {
			return 0;
		}
		if (prices.length == 2) {
			return Math.max(prices[1] - prices[0], 0);
		}
		
        int profit = 0;
        int buy_date = -1;
        
        for (int i = 0; i < prices.length - 1; i++) {
        	if (buy_date < 0) {
				if (prices[i] < prices[i + 1]) {
					buy_date = i;
				}
			} else {
				if (prices[i] > prices[i + 1]) {
					// sell
					profit += prices[i] - prices[buy_date];
					buy_date = -1;
				}
			}
		}
        if (buy_date >= 0) {
            profit += prices[prices.length - 1] - prices[buy_date];
        }
        
        return profit;
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(new BestTimeBuySellStockII().maxProfit(new int[] {1,2,4}));
	}

}
