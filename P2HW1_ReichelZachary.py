# Total of Sale Purchases
# 2/27/22
# CTI-110 P2HW1 - Total Purchases
# Zachary Reichel

#Enter 5 item prices
#Calculate tax on item
#Calculate subtotal before tax
#Calculate total with tax

a = float(input("Enter score #1: "))
b = float(input("Enter score #2: "))
c = float(input("Enter score #3: "))
d = float(input("Enter score #4: "))
e = float(input("Enter score #5: "))
f = float(input("Enter score #6: "))
g = float(input("Enter score #7: "))

subtotal = a + b + c + d + e
            
sales_tax = subtotal * 0.07

total_price = subtotal + sales_tax

print("-------Results-------")
print("Subtotal: {:0.2f}" .format(subtotal))
print("Sales Tax: {:0.2f}".format(sales_tax))
print("Total: {:0.2f}".format(total_price))
