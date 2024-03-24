/**
 * Write a short program that takes as input three integers,
 * a, b and c, from the Java console and determines if they
 * can be used in a correct arithmetic formula(in the given
 * order), like a + b = c, a = b - c, or a * b = c.
 */

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int a, b, c;

		System.out.print("Enter 3 integers in a row: ");
		a = input.nextInt();
		b = input.nextInt();
		c = input.nextInt();

		ArithmeticFormula test = new ArithmeticFormula(a, b, c);

		System.out.println(test.isAdd());
		System.out.println(test.isSub());
		System.out.println(test.isMul());
		System.out.println(test.isDiv());
	}
}

