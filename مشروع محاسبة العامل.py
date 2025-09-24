L = float(input('Enter length: '))
W = float(input('Enter width: '))
price = float(input('Enter price per unit: '))

area = L * W
total_price = area * price

print(f"\nThe area = {L} × {W} = {area}")
print(f"The total price = {total_price}$")