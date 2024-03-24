/**
 * Write a short Java method that takes an array of int values
 * and determines if there is a pair of distinct elements of the
 * array whose product is odd.
 */

public class Main {
	public static void main(String[] args) {
		int[] testArr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
		thereIs2Odds lambda = new thereIs2Odds();
		if (lambda.is2Odds(testArr))
			System.out.println("There is a pair of distinct elements whose product is odd.");
		else
			System.out.println("There is no pair of distinct elements whose product is odd.");
	}
}

