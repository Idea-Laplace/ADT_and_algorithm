public class ArithmeticFormula {
	int a, b, c;

	public ArithmeticFormula() {};
	public ArithmeticFormula(int a, int b, int c) {
		this.a = a;
		this.b = b;
		this.c = c;
	}

	public String isAdd() {
		if (a + b == c)
			return a + "+" + b + "=" + c;
		else if (a == b + c)
			return a + "=" + b + "+" + c;
		else
			return "Not an addition formula.";
	}
	public String isSub() {
		if (a - b == c)
			return a + "-" + b + "=" + c;
		else if (a == b - c)
			return a + "=" + b + "-" + c;
		else
			return "Not a subtraction formula.";
	}
	public String isMul() {
		if (a * b == c)
			return a + "*" + b + "=" + c;
		else if (a == b * c)
			return a + "=" + b + "*" + c;
		else
			return "Not a multiplication formula.";
	}
	public String isDiv() {
		if (b != 0 && a / b == c)
			return a + "/" + b + "=" + c;
		else if (c != 0 && a == b / c)
			return a + "=" + b + "/" + c;
		else
			return "Not a division formula.";
	}
}
