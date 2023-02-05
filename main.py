# This program helps the user calculates annual tax return.

income = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))
# These statements take the input of the customer to make it variable.

chargedFlatRate = 0.2
# All taxpayers are charged a flat tax rate of 20%.

standardDeduction = 10000
# All taxpayers are allowed a $10,000 standard deduction.

dependentDeduction = 3000 * dependents
# For each dependent, a taxpayer is allowed an additional $3,000 deduction.

incomeTax = chargedFlatRate * (income - (standardDeduction + dependentDeduction))
# This statement calculates the total income taxes of the customer.

print(f'The income tax is ${incomeTax:.1f}')
# This statement show the total income tax for the customer.
