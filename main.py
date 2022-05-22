import math
# input
car_price = 65000
down_payment = 10000
loan_term = 72
interest_rate = 6.0

loan_principal = car_price - down_payment
loan_interest = interest_rate / 12 / 100

p = loan_principal
i = loan_interest
n = loan_term

# output
ann_monthly_payment = p * (i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)
ann_monthly_payment = round(ann_monthly_payment, 2)

total_paid = ann_monthly_payment * loan_term + down_payment
interest_paid = total_paid - loan_principal - down_payment

message = f"""You paid for the car = {total_paid},
Your monthly payment = {ann_monthly_payment},
Your loan amount = {loan_principal},
Total interest paid = {math.ceil(interest_paid)},
Loan term = {loan_term} months,
Cost of using a car per month = {round(math.ceil(interest_paid) / loan_term, 2)}."""

print(message)
