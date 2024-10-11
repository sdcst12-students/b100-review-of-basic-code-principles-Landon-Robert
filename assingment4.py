"""
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""

P = float(input("Initial amount borrowed: "))
r = float(input("Monthly interest rate as a decimal: "))
A = float(input("Monthly payment: "))
AmountPaid = 0
total = P
t = 0
interest = 0
while total > AmountPaid:
    total = total - A + P*r
    t = t + 1
    interest = interest + P*r

print(f"{t} months")
print(f"You will have paid ${interest} in interest")