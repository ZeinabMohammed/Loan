#Create DataBase:
class Loan(object):
	"""loan  table"""
	def __init__(self, Amount,period):
		super(Loan, self).__init__()
		self.Amount = Amount
		self.period =period
		self.status='requested'
Lenmo_fee = 3		
class InvestorOffer(Loan):
	"""docstring for Investor"""
	def __init__(self, Amount,period,balance ,annual_interest_rate,fee):
		Loan.__init__(self, Amount,period)
		self.balance=balance
		self.annulal_interest_rate =annual_interest_rate 
		self.monthly_interest_rate = (float(annual_interest_rate /100)/12)
		self.fee=Lenmo_fee
		self.sufficient_balance = Amount+fee
	def has_sufficient_balance(self):
		if self.balance >= self.sufficient_balance:
			print("Investor Offer Accepted")
			status= 'Funded'
			print('Loan status:',status)
			return True
		else:
			status="Rejected"
			print(status)
			print('investor balance is not enough to this process ')
			return False
	def calculate_total_repayments(self):
		return (int(self.monthly_interest_rate * self.period)+ self.fee+self.Amount)
investor_balance = 1000000
investor_offer_annual_interest_rate=15
#Apply use case:
def Lenmo_Loan_System():
	"""A Lenmo borrower would like to borrower some of money on paying them back on number of months period. 
	   One of Lenmo investors has offered him 15% Annual Interest Rate.
	   A $3.00 Lenmo fee will be added to the total loan amount to be paid by the investor."""
	print("*** Welcome To Lenmo Loan System ***")
	loan_offer = InvestorOffer(Amount=(float(input('Please Enter Amount of Dollars You Need To Borrow:'))) ,
				 period=(float(input('How many monthes You will repay it Back?')))
				,balance=investor_balance, annual_interest_rate=investor_offer_annual_interest_rate,fee=Lenmo_fee)
	print(loan_offer.status)
	#check investor balance if it can cover loan and fees
	if loan_offer.has_sufficient_balance():
		loan_offer.status='Funded'
		print('------------------------')
		#scheduled repayments monthly:
		monthly_repayment = (int(loan_offer.monthly_interest_rate+loan_offer.Amount+loan_offer.fee) / loan_offer.period)
		print('Monthly Repayments:', monthly_repayment, '$')
		#Calculate Whole loan repayments:
		total= loan_offer.calculate_total_repayments()
		print('Total Repayments:', total, '$')
		#Complete loan when whole loan repayments refunded:
		if total == ((monthly_repayment )* loan_offer.period):
			loan_offer.status = 'Completed'
			print("Loan Status is :", loan_offer.status)
	else:
		pass

Lenmo_Loan_System()
