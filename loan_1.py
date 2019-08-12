#Import DB:
from models import Loan, InvestorLoanOffer


#use Case initial values:
lenmo_fees=3
loan=Loan(500000,6) #Create loan instance from Loan class with given Amount and period values
loan_offer=InvestorLoanOffer(100000000,15) #use case instance from InvestorLoanOffer class


#check if investor balance covers loan amount and lenmo fees
if loan_offer.investor_balance >= loan.Amount+lenmo_fees:
    loan.status='Funded' 
    print('Your Loan Status:',loan.status)
    
    #calculate Monthly  interest Rate:
    monthly_interest_rate = int((loan_offer.annual_interest_rate /100)/12)
    
    #calculate scheduled Total repays every month:
    monthly_repayment = (int(monthly_interest_rate+loan.Amount+lenmo_fees) / loan.period)
    print("Your Loan Scheduled in system, You should repay",monthly_repayment, "every Month")
    
    #calculate whole Repayments:
    total_repayments = (int(monthly_interest_rate * loan.period)+ lenmo_fees+loan.Amount)
    print('total_repayments:', total_repayments)
   
    #Check if all repayments done succesfully:
    if total_repayments == ((monthly_repayment )* loan.period):
    	loan.status = 'Completed'
    	print('Your Loan is', loan.status ,'successfully')
    else:
    	print('Loan repayments did not Completed! ')

#when investor balance is not enough:
else:
	loan.status="Rejected"
	print(loan.status)
	print('Investor balance is not enough to perform this process ')


