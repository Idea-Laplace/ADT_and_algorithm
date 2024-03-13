public class NumberInfo {
	public NumberInfo() { }
	public boolean isMultiple(long n, long m) {
		if (n == 0 && m != 0)
			return false;
		else if (m == 0)
			return true;
		else if (m % n == 0)
			return true;
		else 
			return false;
	}
	public boolean isOdd(int i) {
		if ((i & 1) != 0)
			return true;
		else
			return false;
	}
	public int APsum(int n) {
		int sum = 0;
		for (int i = 1; i <= n; i++)
			sum += i;
		return sum;
	}
	public int APsum_even(int n) {
		int even_sum = 0;
		for (int i = 2; i <= n; i += 2)
			even_sum += i;
		return even_sum;
	}
	public int square_sum(int n) {
		int sum_of_square = 0;
		for (int i = 1; i * i <= n; i++)
			sum_of_square += i * i;
		return sum_of_square;
	}
}

