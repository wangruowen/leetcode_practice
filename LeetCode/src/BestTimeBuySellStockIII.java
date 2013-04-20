import java.util.ArrayList;

public class BestTimeBuySellStockIII {
	public int maxProfit(int[] prices) {
        int buy_date = 0;
        int max_profit1 = 0, max_profit2 = 0;
        
        ArrayList<Integer> forwardprofit = new ArrayList<Integer>();
        for (int i = 0; i < prices.length; i++) {
			if (prices[i] < prices[buy_date]) {
				buy_date = i;
			}
			int tmp_profit = prices[i] - prices[buy_date];
			if (tmp_profit > max_profit1) max_profit1 = tmp_profit;
			
			forwardprofit.add(max_profit1);
		}
        
        ArrayList<Integer> backwardprofit = new ArrayList<Integer>();
        int sell_date = prices.length - 1;
        for (int j = prices.length - 1; j >= 0; j--) {
			if (prices[j] > prices[sell_date]) {
				sell_date = j;
			}
			int tmp_profit = prices[sell_date] - prices[j];
			if (tmp_profit > max_profit2) max_profit2 = tmp_profit;
			backwardprofit.add(0, max_profit2);
		}
        
        int sum_max_profit = 0;
        for (int i = 0; i < prices.length; i++) {
			int tmp_max_profit = forwardprofit.get(i) + backwardprofit.get(i);
			if (tmp_max_profit > sum_max_profit) sum_max_profit = tmp_max_profit;
		}
        return sum_max_profit;
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
