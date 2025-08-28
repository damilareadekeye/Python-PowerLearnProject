def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If discount is 20% or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: {final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
