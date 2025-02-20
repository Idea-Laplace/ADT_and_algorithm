"""
	R-2.7
	The CreditCard class of Section 2.3 initializes the balacne of a new
	account to zero. Modify that class so that a new aacount can be given
	a nonzero balance using an optional fifth parameter to eh constructor.
	the four-parameter constructor syntax should continue to produce an
	account with zero balance.
"""


class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit, balance=0):
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
        self._balance = balance
    
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
        if amount < 0:
            raise ValueError("amount should be nonnegative.")

        self._balance -= amount

