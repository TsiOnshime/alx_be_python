# Prompt the user for their monthly income.
# The input is converted to a float to allow for decimal values in income.
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses.
# The input is converted to a float to allow for decimal values in expenses.
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings.
# This is done by subtracting the total monthly expenses from the monthly income.
monthly_savings = monthly_income - monthly_expenses

# Define the simple annual interest rate.
# This is a fixed rate of 5%, represented as a decimal (0.05).
annual_interest_rate = 0.05

# Calculate the projected savings after one year, incorporating the interest.
# The formula used is: (Monthly Savings * 12) + (Monthly Savings * 12 * Annual Interest Rate)
# This accounts for the total savings over 12 months plus the interest earned on that amount.
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Display the user's monthly savings.
# The f-string formatting is used to include the calculated monthly_savings value.
print(f"Your monthly savings are ${monthly_savings:.2f}.")

# Display the projected annual savings after including interest.
# The f-string formatting is used to include the calculated projected_annual_savings value,
# rounded to two decimal places for currency representation.
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
