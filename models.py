
# Create Data base:

class Loan(object):
	"""loan table with amount and period attributes"""
	def __init__(self, Amount,period):
		self.Amount = Amount
		self.period =period
		self.status='requested'

class InvestorLoanOffer(object):
	"""loan investor offer table with investor balance and annual interest rate attributes"""
	def __init__(self, investor_balance, annual_interest_rate):
		self.investor_balance = investor_balance
		self.annual_interest_rate=annual_interest_rate
		
