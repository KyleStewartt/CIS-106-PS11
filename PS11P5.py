total = 0
tax = 0.0
def computeTotalAndTax(quantity, unitPrice):
    global total
    total = quantity * unitPrice
    global tax
    tax = total * 0.07
    return total, tax
quantity = int(input("Enter the quantity: "))
unitPrice = float(input("Enter the unit price: "))
computeTotalAndTax(quantity, unitPrice)
print("Total: ", total)
print("Tax: ", tax)