store = {
    "телефон": 10000.00,
    "зубна щітка": 91.50,
    "банан": 44.12,
    "чай": 120.00,
    "зошит": 31.30,
    "ручка": 10.00
}


# 1. Функція форматує ціну
def format_price(price):
    return f"ціна: {price:.2f} грн"


# 2. Функція перевіряє наявність переданих товарів
def check_products(*items):
    return {item: (item in store) for item in items}


# 3. Функція обробляє замовлення
def process_order(order):
    availability = check_products(*order)

    # Перевіряємо чи всі товари є у магазині
    if not all(availability.values()):
        print("\nДеяких товарів немає, замовлення неможливе.")
        missing = [item for item, ok in availability.items() if not ok]
        print("Відсутні товари:", ", ".join(missing))
        return

    # Якщо всі товари є
    total = sum(store[item] for item in order)

    while True:
        action = input("\nЩо хочеш зробити? (купити/ціна): ").lower()

        if action == "ціна":
            print(f"Загальна {format_price(total)}")

        elif action == "купити":
            print("Дякуємо за покупку!")
            break

        else:
            print("Невідома команда. Напишіть 'купити' або 'ціна'.")


# ---------------- ГОЛОВНА ЧАСТИНА ПРОГРАМИ ----------------

print("Товари в магазині:")
for name, price in store.items():
    print(f"- {name}: {format_price(price)}")

order = []

while True:
    items = input("\nВведіть товар (або 'стоп' щоб завершити): ").lower()

    if items == "стоп":
        break

    # Підтримка введення кількох товарів через кому
    for item in items.replace(" ", "").split(","):
        if item in store:
            print(f"Товар доступний, {format_price(store[item])}")

            action = input("Хочеш додати в корзину? (так/ні): ").lower()
            if action == "так":
                order.append(item)
                print(f"{item} додано в корзину.")
        else:
            print(f"Товар '{item}' не знайдено.")

# Після завершення вибору товарів
if not order:
    print("\nВи нічого не вибрали.")
else:
    print("\nВи вибрали:")
    for item in order:
        print(f"- {item}: {format_price(store[item])}")

    # Обробка замовлення
    process_order(order)