public class Main {
	public static void main(String[] args) {
		RemovePunct test = new RemovePunct();
		StringBuilder sb_str;
		sb_str = test.removePunct("Hello, world!");
		System.out.println(sb_str);
	}
}
