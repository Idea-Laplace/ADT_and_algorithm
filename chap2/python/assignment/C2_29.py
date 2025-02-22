"""
C-2.29
Modify the PredatoryCrditCard class from Section 2.4.1 so that
a customer is assigned a minimum monthly payment, as a percentage
of the balance, and so that a late fee is assessed if the customer
does not subsequently pay that minimum amount before the next monthly
cycle.
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
    
    # C-2.29
    def minimum_payment(self):
        minimum = 0
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            minimum = self._balance * (monthly_factor - 1)
        return minimum
