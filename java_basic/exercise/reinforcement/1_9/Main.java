public class Main {
	public static void main(String[] args) {
		Flower f1 = new Flower("rose", 100, 3.60f);

		System.out.println("Name: " + f1.getName());
		System.out.println("Number of petals: " + f1.getPetals());
		System.out.println("Price: " + f1.getPrice());

		f1.setName("lily");
		f1.setPetals(5);
		f1.setPrice(4.7f);

		System.out.println("Name: " + f1.getName());
		System.out.println("Number of petals: " + f1.getPetals());
		System.out.println("Price: " + f1.getPrice());

	}
}
