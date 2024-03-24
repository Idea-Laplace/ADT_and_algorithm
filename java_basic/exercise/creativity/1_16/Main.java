/*
 * Write a short Java program that outputs all possible strings
 * formed by using the characters 'c', 'a', 'r', 'b', 'o' and 'n'
 * exactly once.
 */

import java.util.Scanner;

public class Main {
	public static void main(String[] argv) {
		String sample = argv[0];

		if (sample.length() > 6) {
			System.out.println("Word is too long.");
			return;
		}

		Permutation func = new Permutation(sample);

		func.recursivePermutation(sample, 0);
	}
}

class Permutation {
	// instance variables
	StringBuilder store;
	String original;

	// constructor(s)
	Permutation() {}
	Permutation(String str) {
		original = str;
		store = new StringBuilder(original);
	}

	// setter
	public void setNewString(String str) {
		original = str;
		store = new StringBuilder(original);
	}

	// other method(s)
	public void recursivePermutation(String str, int index) {
		StringBuilder remains = new StringBuilder(str);

		if (index == store.length()) {
			System.out.println(store);
			return;
		}

		for (int i = 0; i < remains.length(); i++) {
			store.setCharAt(index, remains.charAt(i));
			remains.deleteCharAt(i);
			this.recursivePermutation(remains.toString(), index + 1);
			// restore
			remains = new StringBuilder(str);
			if (index == 0)
				System.out.println("");
		}
	}
}



