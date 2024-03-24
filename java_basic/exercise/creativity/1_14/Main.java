/**
 * Wirte a java method that takes an array of int values and determines
 * if all the numbers are different from each other(that is, they are distinct).
 */

import java.util.Arrays;

public class Main {
	public static void main(String[] args) {
		int[] testArr1 = {0, 1, 9, 3, 4, 5, 6, 8, 7, 2};
		int[] testArr2 = {0, 1, 5, 2, 5, 6, 6, 7, 1, 9};
		boolean distinct;

		System.out.println("Array 1: " + Arrays.toString(testArr1));
		System.out.println("Array 2: " + Arrays.toString(testArr2));

		arrInfo instrument = new arrInfo();

		distinct = instrument.isDistinct(testArr1);
		if (distinct)
			System.out.println("Elements in array 1 are distinct.");
		else
			System.out.println("Elements in array 1 are not distinct.");
		
		distinct = instrument.isDistinct(testArr2);
		if (distinct)
			System.out.println("Elements in array 2 are distinct.");
		else
			System.out.println("Elements in array 2 are not distinct.");
	}
}

class arrInfo {
	public arrInfo() {}
	public boolean isDistinct(int[] arr) {
		// arr is called by reference.
		Arrays.sort(arr);
		for (int i = 0; i < arr.length - 1; i++)
			if (arr[i] == arr[i + 1])
				return false;
		return true;
	}
}
