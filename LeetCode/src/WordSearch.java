import java.util.ArrayList;
import java.util.HashMap;

public class WordSearch {
	private class MyChar {
		char name;
		int x, y;

		public MyChar(char name, int x, int y) {
			this.name = name;
			this.x = x;
			this.y = y;
		}
	}

	private HashMap<Character, ArrayList<MyChar>> buildTable(char[][] board) {
		HashMap<Character, ArrayList<MyChar>> table = new HashMap<Character, ArrayList<MyChar>>();
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[i].length; j++) {
				char name = board[i][j];
				MyChar newchar = new MyChar(name, i, j);
				if (table.containsKey(name)) {					
					table.get(name).add(newchar);
				} else {
					ArrayList<MyChar> new_pos_list = new ArrayList<MyChar>();
					new_pos_list.add(newchar);
					table.put(name, new_pos_list);
				}
			}
		}

		return table;
	}

	public boolean exist(char[][] board, String word) {
		HashMap<Character, ArrayList<MyChar>> table = buildTable(board);
		ArrayList<MyChar> visited_chars = new ArrayList<MyChar>();
		return helper(board, table, word, visited_chars);
	}

	private boolean helper(char[][] board,
			HashMap<Character, ArrayList<MyChar>> table, String word,
			ArrayList<MyChar> visited_chars) {
		if (word.length() == 0) {
			return true;
		}

		char first_char = word.charAt(0);
		ArrayList<MyChar> possible_chars = findPossiblePosition(first_char,
				board, table, visited_chars);
		if (possible_chars.isEmpty()) {
			return false;
		} else {
			for (MyChar one_char : possible_chars) {
				ArrayList<MyChar> new_visit_list = new ArrayList<MyChar>(
						visited_chars);
				new_visit_list.add(one_char);
				if (helper(board, table, word.substring(1), new_visit_list)) {
					return true;
				}
			}
		}

		return false;
	}

	private boolean alreadyVisited(ArrayList<MyChar> visited_chars, int x, int y) {
		boolean isVisited = false;
		for (MyChar oneChar : visited_chars) {
			if (oneChar.x == x && oneChar.y == y) {
				isVisited = true;
				break;
			}
		}
		return isVisited;
	}

	private ArrayList<MyChar> findPossiblePosition(char first_char,
			char[][] board, HashMap<Character, ArrayList<MyChar>> table,
			ArrayList<MyChar> visited_chars) {
		ArrayList<MyChar> possible_chars = new ArrayList<MyChar>();
		if (visited_chars.isEmpty()) {
			ArrayList<MyChar> char_list = table.get(first_char);
			if (char_list != null) {
				for (MyChar myChar : char_list) {
					possible_chars.add(myChar);
				}
			}
		} else {
			MyChar lastChar = visited_chars.get(visited_chars.size() - 1);
			int last_x = lastChar.x, last_y = lastChar.y;

			if (last_x > 0) {
				int up_x = last_x - 1;
				int up_y = last_y;
				char up_name = board[up_x][up_y];
				if (up_name == first_char
						&& !alreadyVisited(visited_chars, up_x, up_y)) {
					possible_chars.add(new MyChar(up_name, up_x, up_y));
				}
			}
			if (last_x < board.length - 1) {
				int down_x = last_x + 1;
				int down_y = last_y;
				char down_name = board[down_x][down_y];
				if (down_name == first_char
						&& !alreadyVisited(visited_chars, down_x, down_y)) {
					possible_chars.add(new MyChar(down_name, down_x, down_y));
				}
			}
			if (last_y > 0) {
				int left_x = last_x;
				int left_y = last_y - 1;
				char left_name = board[left_x][left_y];
				if (left_name == first_char
						&& !alreadyVisited(visited_chars, left_x, left_y)) {
					possible_chars.add(new MyChar(left_name, left_x, left_y));
				}
			}
			if (last_y < board[last_x].length - 1) {
				int right_x = last_x;
				int right_y = last_y + 1;
				char right_name = board[right_x][right_y];
				if (right_name == first_char
						&& !alreadyVisited(visited_chars, right_x, right_y)) {
					possible_chars
							.add(new MyChar(right_name, right_x, right_y));
				}
			}
		}

		return possible_chars;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		char[][] board = new char[][] {{'a'}};
		System.out.println(new WordSearch().exist(board, "b"));
	}

}
