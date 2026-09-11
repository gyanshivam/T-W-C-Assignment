# ================================
#  MY BEVERAGE BOOTH
#  File: my-beverage-booth.py
# ================================

# PART 1 — TYPES OF DATA
drink_name   = "Mango Smoothie"   # str   — text
drink_price  = 4.75              # float — decimal
cups_left    = 24                # int   — whole number
is_chilled   = False             # bool  — True or False

print("Drink:", drink_name)
print("Price: $", drink_price)
print("Cups left:", cups_left)
print("Chilled?", is_chilled)

print(type(drink_name))
print(type(drink_price))
print(type(cups_left))
print(type(is_chilled))


# PART 2 — ARITHMETIC OPERATORS
inventory_worth = drink_price * cups_left
print("Inventory worth: $", inventory_worth)
print("Happy hour price: $", drink_price - 1.00)
print("Restock amount:", cups_left + 12)


# PART 3 — COMPARISON OPERATORS
print("Is price below $5?", drink_price < 5)
print("More than 20 cups left?", cups_left > 20)
print("Is price exactly $4.75?", drink_price == 4.75)


# PART 4 — STRING OPERATIONS
booth_name = "Cool" + " " + "Blends"
print("Booth name:", booth_name)
print("Characters in drink name:", len(drink_name))
print("First character:", drink_name[0])


# PART 5 — SWAPPING VALUES
small_price = 3.50
large_price = 5.25
print("Before swap:", small_price, "and", large_price)

temp        = small_price
small_price = large_price
large_price = temp

print("After swap:", small_price, "and", large_price)