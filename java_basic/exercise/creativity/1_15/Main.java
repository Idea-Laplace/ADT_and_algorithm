/*
 * Write a Java method that takes an array containing the set of all integers
 * in the range 1 to 54 and shuffles it into random order. 
 * Your method should output each possible order with equal probability.
 */

import java.util.Arrays;
import java.util.Random;

public class Main {
	public static void main(String[] args) {
		Random random = new Random();
		int[] array = new int[54];
		int temp, rand_index;

		random.setSeed(System.currentTimeMillis());

		for (int i = 0; i < array.length; i++)
			array[i] = i + 1;

		for (int i = array.length - 1; i > 0; i--) {
			rand_index = random.nextInt(i);
			temp = array[i];
			array[i] = array[rand_index];
			array[rand_index] = temp;
		}

		System.out.println("Array: " + Arrays.toString(array));
	}
}
