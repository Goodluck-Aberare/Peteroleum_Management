
import sqlite3
from datetime import datetime

# Connect to the database
connection = sqlite3.connect("petroleum_logistics.db")
cursor = connection.cursor()


# 1. Create database tables
def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL UNIQUE,
            quantity REAL DEFAULT 0,
            unit_price REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trucks (
            truck_id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate_number TEXT NOT NULL UNIQUE,
            driver_name TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS deliveries (
            delivery_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            truck_id INTEGER,
            quantity REAL NOT NULL,
            destination TEXT NOT NULL,
            delivery_date TEXT,
            FOREIGN KEY (product_id) REFERENCES products(product_id),
            FOREIGN KEY (truck_id) REFERENCES trucks(truck_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_type TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT,
            transaction_date TEXT
        )
    """)

    connection.commit()


# 2. Register petroleum products
def add_product():
    name = input("Enter product name (PMS, AGO, DPK): ").upper()

    try:
        quantity = float(input("Enter initial quantity (litres): "))
        price = float(input("Enter unit price per litre (NGN): "))

        if quantity < 0 or price <= 0:
            print("Quantity cannot be negative and price must be positive.")
            return

        cursor.execute("""
            INSERT INTO products (product_name, quantity, unit_price)
            VALUES (?, ?, ?)
        """, (name, quantity, price))

        connection.commit()
        print("Product registered successfully!")

    except sqlite3.IntegrityError:
        print("This product already exists.")
    except ValueError:
        print("Please enter valid numbers.")


# 3. Register trucks and drivers
def add_truck():
    plate = input("Enter truck plate number: ").upper()
    driver = input("Enter driver's name: ")

    try:
        cursor.execute("""
            INSERT INTO trucks (plate_number, driver_name)
            VALUES (?, ?)
        """, (plate, driver))

        connection.commit()
        print("Truck registered successfully!")

    except sqlite3.IntegrityError:
        print("This truck is already registered.")


# 4. Record a petroleum delivery
def record_delivery():
    try:
        product_id = int(input("Enter product ID: "))
        truck_id = int(input("Enter truck ID: "))
        quantity = float(input("Enter delivery quantity (litres): "))
        destination = input("Enter delivery destination: ")

        if quantity <= 0:
            print("Delivery quantity must be greater than zero.")
            return

        cursor.execute("""
            SELECT quantity, unit_price
            FROM products WHERE product_id = ?
        """, (product_id,))

        product = cursor.fetchone()

        if product is None:
            print("Product not found.")
            return

        if product[0] < quantity:
            print("Insufficient inventory!")
            return

        cursor.execute("""
            SELECT truck_id FROM trucks WHERE truck_id = ?
        """, (truck_id,))

        if cursor.fetchone() is None:
            print("Truck not found.")
            return

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Record the delivery
        cursor.execute("""
            INSERT INTO deliveries
            (product_id, truck_id, quantity, destination, delivery_date)
            VALUES (?, ?, ?, ?, ?)
        """, (product_id, truck_id, quantity, destination, date))

        # Reduce available inventory
        cursor.execute("""
            UPDATE products
            SET quantity = quantity - ?
            WHERE product_id = ?
        """, (quantity, product_id))

        # Record the transaction
        amount = quantity * product[1]

        cursor.execute("""
            INSERT INTO transactions
            (transaction_type, amount, description, transaction_date)
            VALUES (?, ?, ?, ?)
        """, ("DELIVERY", amount, destination, date))

        connection.commit()
        print("Delivery recorded successfully!")
        print(f"Delivery value: NGN {amount:,.2f}")

    except ValueError:
        connection.rollback()
        print("Please enter valid numerical values.")


# 5. View available inventory
def view_inventory():
    cursor.execute("""
        SELECT product_id, product_name, quantity, unit_price
        FROM products
        ORDER BY product_id
    """)

    products = cursor.fetchall()

    print("\n========== PETROLEUM INVENTORY ==========")

    if not products:
        print("No products registered.")
        return

    for product in products:
        print(f"""
Product ID: {product[0]}
Product: {product[1]}
Available Quantity: {product[2]:,.2f} litres
Unit Price: NGN {product[3]:,.2f}
Stock Value: NGN {product[2] * product[3]:,.2f}
-------------------------------------------
""")


# 6. View registered trucks
def view_trucks():
    cursor.execute("""
        SELECT truck_id, plate_number, driver_name
        FROM trucks
    """)

    trucks = cursor.fetchall()

    print("\n========== REGISTERED TRUCKS ==========")

    for truck in trucks:
        print(f"ID: {truck[0]} | Plate: {truck[1]} | Driver: {truck[2]}")

    if not trucks:
        print("No trucks registered.")


# 7. View delivery reports
def delivery_report():
    cursor.execute("""
        SELECT
            deliveries.delivery_id,
            products.product_name,
            trucks.plate_number,
            deliveries.quantity,
            deliveries.destination,
            deliveries.delivery_date
        FROM deliveries
        JOIN products
        ON deliveries.product_id = products.product_id
        JOIN trucks
        ON deliveries.truck_id = trucks.truck_id
        ORDER BY deliveries.delivery_id DESC
    """)

    records = cursor.fetchall()

    print("\n========== DELIVERY REPORT ==========")

    for record in records:
        print(
            f"Delivery ID: {record[0]} | "
            f"Product: {record[1]} | "
            f"Truck: {record[2]} | "
            f"Quantity: {record[3]:,.2f} litres | "
            f"Destination: {record[4]} | "
            f"Date: {record[5]}"
        )

    if not records:
        print("No delivery records available.")


# 8. View financial summary
def financial_report():
    cursor.execute("""
        SELECT transaction_type, SUM(amount)
        FROM transactions
        GROUP BY transaction_type
    """)

    records = cursor.fetchall()

    print("\n========== FINANCIAL SUMMARY ==========")

    if not records:
        print("No financial transactions recorded.")
        return

    for record in records:
        print(f"{record[0]}: NGN {record[1]:,.2f}")


# 9. Main application menu
def main():
    create_tables()

    while True:
        print("""
=========================================
 PETROLEUM LOGISTICS MANAGEMENT SYSTEM
=========================================

1. Register Petroleum Product
2. Register Truck and Driver
3. Record Petroleum Delivery
4. View Inventory
5. View Registered Trucks
6. View Delivery Reports
7. View Financial Summary
8. Exit
""")

        choice = input("Select an option (1-8): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            add_truck()
        elif choice == "3":
            record_delivery()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            view_trucks()
        elif choice == "6":
            delivery_report()
        elif choice == "7":
            financial_report()
        elif choice == "8":
            connection.close()
            print("Thank you for using the system!")
            break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()
