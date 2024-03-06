public class Counter {
	private int count;
	public Counter() {};    // Default constructor, count is 0
	public Counter(int initial) { count = initial; } // An alternative constructor
	public int getCount() { return count; } // An accessor method, getter.
	public void increment() { count++; }    // An update method
	public void increment(int delta) { count += delta; } // An update method
	public void reset() { count = 0; }
}
