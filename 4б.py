store = {
    "телефон": 10000.00,
    "зубна щітка": 91.50,
    "банан": 44.12,
    "чай": 120.00,
    "зошит": 31.30,
    "ручка": 10.00
}

print("Товари в магазині:")
for name, price in store.items():
    print(f"- {name}: {price} грн")

order = []

while True:
    item = input("\nВведіть товар (або 'стоп' щоб завершити): ").lower()

    if item == "стоп":
        break

    if item in store:
        print(f"Товар доступний. Ціна: {store[item]} грн")

        action = input("Хочеш додати в корзину? (так/ні): ").lower()

        if action == "так":
            order.append(item)
            print(f"{item} додано в корзину.")
    else:
        print("На жаль, такого товару немає в магазині.")

# Після завершення вводу
if not order:
    print("\nВи нічого не вибрали.")
else:
    print("\nУ вашій корзині:")
    for item in order:
        print(f"- {item}: {store[item]} грн")

    total = sum(store[item] for item in order)
    print(f"Загальна сума: {total} грн")

    buy = input("Купити ці товари? (так/ні): ")

    if buy.lower() == "так":
        print("Дякуємо за покупку!")
    else:
        print("Покупку скасовано.")

