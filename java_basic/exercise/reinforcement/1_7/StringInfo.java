public class StringInfo {
	static final char[] vowel = {'A', 'E', 'I', 'O', 'U',
								 'a', 'e', 'i', 'o', 'u'};
	static final int VOWELS = 10;
	public StringInfo() {};
	public int CountVowel(String str) {
		int count = 0;
		for (int i = 0; i < str.length(); i++)
			for (int j = 0; j < VOWELS; j++)
				if (str.charAt(i) == vowel[j]) {
					count++;
					break;
				}
		return count;
	}
}


