public class TestStringInfo {
	public static void main(String[] args) {
		StringInfo test = new StringInfo();

		String test_str = "Hello, World!";
		int vowels = test.CountVowel(test_str);

		System.out.println(test_str);
		System.out.println("Number of vowels: " + Integer.toString(vowels));
	}
}
