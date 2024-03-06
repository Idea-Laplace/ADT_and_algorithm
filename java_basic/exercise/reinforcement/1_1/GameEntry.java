/**
 * Suppose that we create an array A of GameEntry objects, which has an integer
 * scores field, and we clone A and store the result in an array B. If we then
 * immediately set A[4], score equal to 550, what is the score value of the Ga-
 * meEntry object referenced by B[4]?
 */

public class GameEntry {
	int score;
	public GameEntry() { score = 0; }
	public GameEntry(int score) {
		this.score = score;
	}
	public void SetScore(int score) {
		this.score = score;
	}

	public String Score2String() {
		return Integer.toString(score);
	}
}

