public class thereIs2Odds {
	public thereIs2Odds() {}
	public boolean is2Odds(int[] arr) {
		int num_odds = 0;
		for (int element : arr)
			if (element % 2 != 0)
				num_odds++;
		if (num_odds >= 2)
			return true;
		else
			return false;
	}
}

