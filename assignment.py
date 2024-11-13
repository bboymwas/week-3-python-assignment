# Function for calculating discount
def calculate_discount(price,discount_percent):
    if discount_percent>=20:
           discount_amount = price * (discount_percent/100)
           final_price = price - discount_amount
           return final_price
    else:
          return price
#Asking input from the 
try: 
      original_price = float(input("Enter the original price of the item:"))
      percentage_discount =float(input("Enter the percentage discount of the item:")) 
      # calling the function
      final_price = calculate_discount(original_price,percentage_discount)
      # print the final price
      if  original_price == final_price:
         print(f"No discount given.The original price is: ${final_price:.2f}")
      else:
           print(f"The final price after applying the discount is: ${final_price:.2f}")

except ValueError:
      print("Please enter valid numeric values for price and discount percentage")

 