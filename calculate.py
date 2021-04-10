
intrestRate = 0.07
loanTenure = 5
loanAmount = 10000000

intrest = loanAmount * intrestRate
print("intrest: ", intrest)
loanAmount = loanAmount + (intrest * loanTenure)
print("loanAmount: ",loanAmount)
monthlyCaclulation = loanAmount / (loanTenure * 12)
print("monthlyCaclulation: ",monthlyCaclulation)
