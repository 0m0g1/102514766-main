price = 50
paid = 0

while price > 0:
    print(f"Amount Due: {price}")
    pay = int(input("Insert Coin: "))
    if pay in [25, 10, 5]:
        price = price - pay
        paid = paid + pay

if paid >= price:
    print(f"Change Owed: {paid - 50}")