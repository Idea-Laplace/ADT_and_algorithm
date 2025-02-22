"""
C-2.28
The PredatoryCreditCard class of Section 2.4.1 provides a 
process_month method that models the completion of a monthly
cycle. Modify the class so that once a customer has made ten
calls to charge in the current month, each additional call to
that function results in an additional $1 surcharge.
"""
import sys
sys.path.append("..")   
from CreditCard import CreditCard

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new prodatory credit card instance.
        
        The initial balance is zero.
        
        customer    The name of the customer(e.g. 'John Doe')
        bank        The name of the bank(e.g., 'California Savings'
        acnt        The account identifier
        limit       Credit limit (measured in dollars)
        apr         annual percentage rate(e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        # C-2.28
        self._charge_count = 0

    def charge(self, price):
        success = super().charge(price)
        # C-2.28
        if self._charge_count >= 10:
            self._balance += 1

        if not success:
            self._balance += 5

        # C-2.28
        self._charge_count += 1
        return success
    
    # Extension
    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # If positive balance, convert APR to monthly multiplication factor.
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor
            # C-2.28
            self._charge_count = 0