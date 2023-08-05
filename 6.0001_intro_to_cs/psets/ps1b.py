# Assignment Part B : House Hunting, with raise
# This program computes how many months to buy your dream house using your annual salary and allocation savings

# Constants
portion_down_payment = 0.25     # Downpayment Percentage
current_savings = 0             # Current money in your bank account
r = 0.04                        # Investment Return Percent

# User Inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost    = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual rase, as a decimal: "))
 

monthly_salary = annual_salary / 12 
down_payment = total_cost * portion_down_payment

num_months = 0

while down_payment - current_savings > 0:
    current_savings = current_savings + monthly_salary * portion_saved + (current_savings * r / 12)
    # 6th month raise should reflect on the NEXT monthly salary
    if num_months != 0 and (num_months % 6) == 0:
        monthly_salary = monthly_salary * (1 + semi_annual_raise)
    num_months += 1


print("Number of months:", num_months)    



