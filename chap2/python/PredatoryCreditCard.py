from CreditCard import CreditCard

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new prodatory credit card instance.
        
        The initial balance is zero.
        
        customer    The name of the customer(e.g. 'John Doe')
        bank        The name of the bank(e.g., 'California Savings'
        acnt        The account identifier
        limit       Credit limit (measured in dollars)
        apr         annual percentage rate(e.g., 0.0825 for 8.25% APR)
        """

        # Call super constructor
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    # Method Overriding
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit
        
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """

        # Call inherited method.
        success = super().charge(price)
        # Assess penalty.
        if not success:
            self._balance += 5
            return success
        return success
    
    # Extension
    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # If positive balance, convert APR to monthly multiplication factor.
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor