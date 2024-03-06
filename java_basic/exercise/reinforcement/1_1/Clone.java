public class Clone {
	public static void main(String[] args) {
		GameEntry[] A = new GameEntry[5];
		GameEntry[] B = A;

		for (int i = 0; i < 5; i++)
			A[i] = new GameEntry();

		System.out.println("A[4] = " + A[4].Score2String());
		System.out.println("B[4] = " + A[4].Score2String());

		A[4].SetScore(550);

		System.out.println("After set A[4] = 550");
		System.out.println("A[4] = " + A[4].Score2String());
		System.out.println("B[4] = " + A[4].Score2String());
	}
}
		

