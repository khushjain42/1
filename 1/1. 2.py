"""Write a python program to compute a person's income tax. Assume following tax laws:
• All taxpayers are charged a flat tax rate of 20%.
• All taxpayers are allowed a $10,000 standard deduction.
• For each dependent, a taxpayer is allowed an additional $3,000 deduction.
• Gross income must be entered to the nearest penny.
Gross Income and the number of dependents must be asked from the user. Hint:
Taxable income = Gross Income - Standard deduction - (Dependent deduction
* No. of dependents)
Tax = Taxable Income * Tax Rate"""
x=float(input("please enter your gross income"))
y=float(input("please enter your no. of dependents"))
print("flat taxable amount",x/5)
print(" standard deduction $10000")
print("additional tax due to no. of dependents",3000*y)
print("Total taxable income",x-10000-(3000*y))
