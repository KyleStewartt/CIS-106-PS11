def computeDiscountedPrice(quantity, price, discountRate):
    discountAmount = price * discountRate / 100
    discountedPrice = price - discountAmount
    return discountAmount, discountedPrice
quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price: "))
discountRate = float(input("Enter the discount rate: "))
discountAmount, discountedPrice = computeDiscountedPrice(quantity, price, discountRate)
print("Quantity: ", quantity)
print("Price: ", price)
print("Discount Amount: ", discountAmount)
print("Discounted Price: ", discountedPrice)