# Sales Summary Calculator
# Concepts: user input, f-string, type cast, user-defined function

def sales_summary(name, region, units, price):
 revenue = units * price      #total revenue
 bonus = revenue * 0.10       # 10% performance bonus
 return revenue, bonus

# ── Collect input ──────────────────────────────────────
name = input("Associate name: ")
region = input("Store region: ")
units = int (input("Units sold: "))         # cast str -> int
price = float(input("Price per unit $: "))  # cast str -> float

# ── Call the function ──────────────────────────────────
revenue, bonus = sales_summary(name, region, units, price)

# ── Print formatted report ─────────────────────────────
print(f"""
===== RetailEdge Inc. — Sales Summary =====
Associate : {name}
Region : {region}
Units sold: {units}
Unit price: ${price:.2f}
-------------------------------------------
Total revenue           : ${revenue:.2f}
Performance bonus (10%) : ${bonus:.2f}
===========================================
""")


# 5. Add input validation using try / except to catch non-numeric entries for units and 
price

while True:
    try:
        units = int(input("Units sold: "))
        break
    except ValueError:
        print("Invalid! Please enter a whole number.")

while True:
    try:
        price = float(input("Price per unit $: "))
        break
    except ValueError:
        print("Invalid! Please enter a number.")
        
# try = attempts to convert the input to a number
# except ValueError = if the user types letters like "abc", it catches the error and prints a message
# while True = keeps asking until a valid number is entered
# break = exits the loop once valid input is given
