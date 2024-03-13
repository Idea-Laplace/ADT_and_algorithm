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
		if (i % 2 == 0)
			return true;
		else
			return false;
	}
}

