public class CounterDemo {
	public static void main(String[] args) {
		Counter c;
		c = new Counter();
		c.increment();
		c.increment(3);
		int temp = c.getCount();
		c.reset();
		Counter d = new Counter(5);
		d.increment();
		Counter e = d;
		temp = e.getCount();
		e.increment(2);
	}
}

class Counter {
	private int count;
	public Counter() {};    // Default constructor, count is 0
	public Counter(int initial) { count = initial; } // An alternative constructor
	public int getCount() { return count; } // An accessor method, getter.
	public void increment() { count++; }    // An update method
	public void increment(int delta) { count += delta; } // An update method
	public void reset() { count = 0; }
}
