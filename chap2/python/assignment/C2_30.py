"""
C-2.30
At the close of Section 2.4.1, we suggest a model in which the CreditCard
class supports a nonpublic method, _set_balance(b), that could be used by
subclasses to affect a change to the balance, without directly accessing the
_balance data member. Implement such a model, revising both the CreditCard
and PredatoryCreditCard classes accordingly."""


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
            self._set_balance(1)

        if not success:
            self._set_balance(5)

        # C-2.28
        self._charge_count += 1
        return success
    
    # Extension
    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # If positive balance, convert APR to monthly multiplication factor.
            monthly_factor = pow(1+self._apr, 1/12)
            fee = (monthly_factor - 1) * self._balance
            self._set_balance(fee)
            # C-2.28
            self._charge_count = 0
    
    # C-2.29
    def minimum_payment(self):
        minimum = 0
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            minimum = self._balance * (monthly_factor - 1)
        return minimum
