/*
 * Write a short Java program that takes 2 arrays a and b
 * of length n storing int values, and returns the dot product
 * of a and b, That is, it returns an array of c of length n 
 * such that c[i] = a[i] * b[i].
 */

import java.util.Random;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) {
		final int limit = 10;
		final int length = 7;
		Random random = new Random();

		int[] a = new int[length];
		int[] b = new int[length];
		int[] c = new int[length];

		for (int i = 0; i < length; i++) {
			a[i] = random.nextInt(limit);
			b[i] = random.nextInt(limit);
			c[i] = a[i] * b[i];
		}

		System.out.println("a: " + Arrays.toString(a));
		System.out.println("b: " + Arrays.toString(b));
		System.out.println("c: " + Arrays.toString(c));
	}
}

