# Assignment Part C : House Hunting, with raise
# This program computes the best percentage of your salary (in months) to save to pay the downpayment in 36 months 

# Constants
portion_down_payment = 0.25     # Downpayment Percentage
current_savings = 0             # Current money in your bank account
r = 0.04                        # Investment Return Percent
total_cost    = 1e6             # Total Cost of the house
semi_annual_raise = 0.07        # Bi-annual Salary Raise
num_year_goal = 3               # Number of Years to save for down payment of house

# User Inputs
annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary / 12 
num_months_goal = num_year_goal * 12 

num_months = 0
num_steps  = 0
down_payment = total_cost * portion_down_payment

portion_saved_low  = 0      # Range start with 0%  of Salary is saved (in months)
portion_saved_high = 10000  # Range ends with 100% of Salary is saved (in months)
portion_saved_current = 0   # Current Percentage Iteration

epsilon = 100   # Allowable Devation from down_pament

while abs(down_payment - current_savings) >= epsilon:
    print(portion_saved_high, portion_saved_low, portion_saved_current)
    portion_saved_current = (portion_saved_high + portion_saved_low) / 2 # Current Interest Rate Iteration     
    
    # Reset to Initial Values
    monthly_salary = annual_salary / 12
    current_savings = 0
    num_months = 0
     
    while  num_months_goal > num_months and (down_payment - current_savings) > epsilon:
        current_savings = current_savings + (monthly_salary * portion_saved_current / 10000) + (current_savings * r / 12)
        if num_months != 0 and (num_months % 6) == 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
        num_months += 1
           
    if down_payment - current_savings >= 0:
        portion_saved_low = portion_saved_current
    else:
        portion_saved_high = portion_saved_current
    num_steps += 1
    
    if(portion_saved_high - portion_saved_low < .01): break
    
        
if (portion_saved_high - portion_saved_low < 1):
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best Savings Rate:", portion_saved_current / 10000);
    print("Steps in Bisection search", num_steps)
    



