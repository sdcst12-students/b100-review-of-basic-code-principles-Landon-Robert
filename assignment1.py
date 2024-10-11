"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

P = float(input("Initial Amount: "))
r = float(input("Rate as a decimal: "))
Unit = (input("Time unit (days, months, years, eons): "))
if Unit == "years":
  n = 1
elif Unit == "months":
  n = 12
elif Unit == "days":
  n = 365
elif Unit == "eons":
  n = 0.0000000001
elif Unit != "days" and Unit != "months" and Unit != "years" and Unit != "eons":
  print("That is not a valid unit")
t = float(input("Time amount: "))
I = P*r*t/n
print(f"Your total interest is ${round(I,2)}.")