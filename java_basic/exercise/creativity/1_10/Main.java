/**
 * Write a pseudocode description of a method for finding
 * the smallest and largest numbers in an array of integers
 * and compare that to a Java mehtod that would do the same
 * thing.
 */

import java.util.Arrays;

public class Main {
	public static void main(String[] args) {
		int[] arr = {3, 1, 4, 5, 9, 2, 6, 8, 7, 0};
		// variables for smallest and lagest value of an array.
		int min, max;

		// Initialization of min and max
		min = max = arr[0];

		// Comparison loop
		// array.length vs string.length(), instance variable versus method
		for (int i = 0; i < arr.length; i++) {
			min = min < arr[i] ? min : arr[i];
			max = max > arr[i] ? max : arr[i];
		}

		System.out.println(Arrays.toString(arr));
		System.out.println("Largest: " + max);
		System.out.println("Smallest: " + min);
	}
}


