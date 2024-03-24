/**
 * Write a Java program that can take a positive integer greater than 2
 * as input and write out the number of times one must repeatedly divide
 * this numiber by 2 before getting a value less than 2.
 */

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int num;
		int count = 0;

		System.out.print("Enter a positive integer(larger than 2): ");
		num = input.nextInt();
		while (num >= 2) {
			num /= 2;
			count++;
		}

		System.out.println("Number of division times: " + count);
	}
}




