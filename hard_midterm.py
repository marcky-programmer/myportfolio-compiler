loan = eval(input( "Enter  loan amount --> "))
loan_period = eval(input("Enter a period in year"))
months = loan_period * 12
principal = loan / months
balance = loan

print("Months\t|\tPrincipal Payment\t|\tRemaining Balance\t|\tInterest\t|\tMonthly Payment")

for i in range(1,months + 1,1):
    balance -= principal
    interest = balance * 0.03
    monthly = principal + interest
    print(f"{i}\t|\t\t{round(principal,2)}\t\t|\t\t{round(interest,2)} \t\t|\t{round(balance,2)}\t\t|\t\t{round(monthly,2)}")

