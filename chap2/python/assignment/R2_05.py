"""
	R-2.5
	Use the technique of Section 1.7 to revise the charge and make_payment
	methods of the CreditCard class to ensure that the caller sends a number
	as a parameter.
"""


class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.
        
        the initial balance is zero.

        customer  The name of the customer.
        bank      The name of the bank.
        acnt      The account identifier.
        limit     credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    
    # Accessors
    def get_customer(self):
        """Return name of the customer"""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number(typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit
    
    def get_balance(self):
        """Return current balance."""
        return self._balance

    # mutators
    def charge(self, price):
        """Charge given price to the cardm assuming sufficient credit limit.
        
        Return True if charge was processed; False if charge was denied.
        """

        if not isinstance(price, (int, float)):
            raise TypeError("price must be numeric.")

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be numeric.")

        self._balance -= amount


