public class Flower {
	// Instance variables
	String name;
	int petals;
	float price;

	// Constructor
	public Flower() {};
	public Flower(String name, int petals, float price) {
		this.name = name;
		this.petals = petals;
		this.price = price;
	}

	// Setter
	void setName(String name) { this.name = name; }
	void setPetals(int petals) { this.petals = petals; }
	void setPrice(float price) { this.price = price; }

	// Getter
	String getName() { return name; }
	int getPetals() { return petals; }
	float getPrice() { return price; }
}



