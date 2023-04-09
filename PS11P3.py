def computeCommissionAndTarget(sales):
    if sales > 100000:
        commission = sales * 0.1
    else:
        commission = sales * 0.05
    nextYearTarget = sales * 0.05
    return commission, nextYearTarget
lastName = input("Enter the salesperson's last name: ")
sales = float(input("Enter the sales amount: "))
commission, nextYearTarget = computeCommissionAndTarget(sales)
print("Salesperson's Name: ", lastName)
print("Commission: ", commission)
print("Next Year's Target: ", nextYearTarget)