public class Test {
	public static void main(String[] args) {
		NumberInfo test = new NumberInfo();
		if (test.isMultiple(2, 4))
			System.out.println("4 is a multiple of 2.");
		if (test.isMultiple(2, 3) == false)
			System.out.println("3 is not a multiple of 2.");
		if (test.isOdd(3))
			System.out.println("3 is odd.");
		if (test.isOdd(4) == false)
			System.out.println("4 is even.");
		int sum = test.APsum(100);
		System.out.println(Integer.toString(sum));
		sum = test.APsum_even(100);
		System.out.println(Integer.toString(sum));
		sum = test.square_sum(100);
		System.out.println(Integer.toString(sum));
	}
}

