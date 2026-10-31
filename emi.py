def loan_emi(amount,duration,rate,down_payment=0):
    loan_amount=amount-down_payment
    emi=loan_amount*rate*((1+rate)**duration)/(((1+rate)**duration)-1)
    return round(emi,2)
    
    
amount=float(input("Enter amount:"))
duration=float(input("Enter duration:"))
rate=float(input("Enter rate:"))
down_payment=float(input("Enter downpayment:"))
print("Emi is:",loan_emi(amount,duration,rate,down_payment))
