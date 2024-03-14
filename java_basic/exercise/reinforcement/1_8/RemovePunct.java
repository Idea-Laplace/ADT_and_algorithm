public class RemovePunct {
	private static String punctuations = ".,?!`\'";
	public RemovePunct() {}
	public StringBuilder removePunct(String s) {
		StringBuilder sb_s = new StringBuilder(s);
		for (int i = 0; i < sb_s.length(); i++)
			for (int j = 0; j < punctuations.length(); j++)
				if (sb_s.charAt(i) == punctuations.charAt(j)) {
					sb_s.setCharAt(i, '\0');
					break;
				}

		return sb_s;
	}
}


