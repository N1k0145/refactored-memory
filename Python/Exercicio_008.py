from decimal import Decimal

meters = Decimal(input("Digite uma distância, em metros: "))

kilometers = (meters / Decimal('1000'))
centimeters = (meters * Decimal('100'))
millimeters = (meters * Decimal('1000'))

print(f"A distância de {meters}m corresponde a :")
print(f"{kilometers:<10.5f} Km.")
print(f"{centimeters:<10} cm.")
print(f"{millimeters:<10} mm.")