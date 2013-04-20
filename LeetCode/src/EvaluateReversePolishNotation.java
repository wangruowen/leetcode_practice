import java.util.Stack;

public class EvaluateReversePolishNotation {
	public int evaluateReversePolishNotation(String[] exp) {
		Stack<Integer> stack = new Stack<Integer>();

		for (int i = 0; i < exp.length; i++) {
			if (exp[i].matches("[\\d]+")) {
				stack.push(Integer.parseInt(exp[i]));
			} else {
				int op2 = stack.pop();
				int op1 = stack.pop();
				int result = 0;
				switch (exp[i]) {
				case "+":
					result = op1 + op2;
					break;
				case "-":
					result = op1 - op2;
					break;
				case "*":
					result = op1 * op2;
					break;
				case "/":
					result = op1 / op2;
					break;
				}
				stack.push(result);
			}
		}
		return stack.pop();
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(new EvaluateReversePolishNotation().evaluateReversePolishNotation(new String[] {"5", "8", "4", "/", "+"}));
	}

}
