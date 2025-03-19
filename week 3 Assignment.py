def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        discount_amount = (discount_percent * price) / 100
        final_price=price-discount_amount
        print(f"Price is {final_price}")

    else :
        print(f"Price is {price}")

price=float(input("Enter price :"))
discount_percent=float(input("Enter discount:"))
calculate_discount(price, discount_percent)
print(f"Original price is : {price} ")