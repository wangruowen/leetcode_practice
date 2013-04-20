import java.util.ArrayList;

public class SimplifyPath {
	public String simplifyPath(String path) {
		ArrayList<String> path_list = new ArrayList<String>();
		int index1, index2;
		path += "/";
		index1 = path.indexOf('/');
		while ((index2 = path.indexOf('/', index1 + 1)) >= 0) {
			String one_dir = path.substring(index1 + 1, index2);
			if (!one_dir.equals(".") && !one_dir.equals("")) {
				if (one_dir.equals("..") && !path_list.isEmpty()) {
					path_list.remove(path_list.size() - 1);
				} else  {
					//if (one_dir.matches("[\\p{Alnum}\\p{Space}\\.]+"))
					path_list.add(one_dir);
				}
			}
			index1 = index2;
		}
		String simplified_path = "/";
		for (int i = 0; i < path_list.size(); i++) {
			simplified_path += path_list.get(i);
			if (i < path_list.size() - 1) {
				simplified_path += '/';
			}
		}
		return simplified_path;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(new SimplifyPath().simplifyPath("/.hidden"));
	}

}
