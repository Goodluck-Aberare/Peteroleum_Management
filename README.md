# Petroleum Logistics and Inventory Management System

## Overview
My name is Goodluck Aberare, and I am an aspiring software engineer passionate about developing my programming, database management, and problem-solving skills. As part of my journey toward becoming a skilled software developer, I developed this Petroleum Logistics and Inventory Management System to gain practical experience in building software applications that solve real-world business problems. The Petroleum Logistics and Inventory Management System is a Python-based application integrated with an SQLite relational database. It is designed to manage petroleum products, truck and driver information, delivery records, and financial transactions.

The application allows users to:
- Add and manage petroleum products, including their quantities and unit prices.
- Register trucks and their corresponding drivers.
- Record petroleum deliveries, including destinations, quantities, and delivery dates.
- Monitor available petroleum inventory.
- Automatically update inventory quantities after deliveries.
- Generate delivery reports by retrieving information from related database tables.
- View financial summaries of recorded transactions.

To use the program, run the Python file from the terminal using the command `python petroleum_management.py`. The application displays a menu that allows users to select different operations and manage their logistics records. The SQLite database is created automatically when the program runs.

**Purpose of the Project**
My purpose for developing this software is to understand how Python applications interact with relational databases to organize, store, retrieve, and manage information. The petroleum logistics industry involves handling large quantities of products, transportation activities, deliveries, and financial records. Managing these activities manually can lead to errors, poor record keeping, and difficulties monitoring inventory. Through this project, I aim to develop my software engineering skills by applying programming concepts and SQL operations to a practical industry challenge. I also want to improve my understanding of database relationships, application development, and problem-solving.

**Software Demonstration Video**
[Software Demo Video] https://www.loom.com/share/5be947e9d83f44449ffda82e8f30edf3

## Relational Database
The application uses **SQLite**, a lightweight relational database management system, to store and manage information. I used Python's built-in `sqlite3` library to establish a connection between the application and the database. The database is designed to organize information into related tables. This structure reduces unnecessary data duplication and makes it easier to retrieve information from different sections of the application.

**Database Structure**
The relational database contains the following main tables:

1. **Products Table:** Stores petroleum product information, including product names, available quantities, and unit prices.
2. **Trucks Table:** Stores truck registration details and information about the vehicles used for petroleum transportation.
3. **Drivers Table:** Stores driver information associated with the transportation process.
4. **Deliveries Table:** Records delivery transactions, including the product delivered, truck used, destination, quantity, and delivery date.
5. **Financial Transactions Table:** Stores financial information associated with recorded deliveries and transactions.

**Database Relationships and Operations**
The database uses primary keys to uniquely identify records and foreign keys to establish relationships between related tables. For example, delivery records can reference the corresponding products and trucks involved in each transaction.

I used SQL operations such as:
- `CREATE TABLE` to create database tables.
- `INSERT` to add new records.
- `SELECT` to retrieve stored information.
- `UPDATE` to modify existing records and inventory quantities.
- `JOIN` to retrieve related information from multiple tables.
- Aggregate functions to generate financial summaries and reports.

Working with SQLite has helped me understand how relational databases support software applications and how structured data can improve business operations.

## Development Environment
I used the following tools and technologies to develop this software:
- **Visual Studio Code (VS Code):** Used as the primary code editor for writing, editing, debugging, and running the Python application.
- **Python:** The programming language used to develop the application and implement its functionalities.
- **SQLite:** Used as the relational database management system for storing and managing application data.
- **SQLite3 Library:** Python's built-in library used to connect the application to the SQLite database and execute SQL queries.
- **Git:** Used for version control and tracking changes during development.
- **GitHub:** Used to store, manage, and share the project repository.
- **Terminal:** Used to execute the Python program and interact with the application.

**Programming Language**
The programming language used for this project is Python. Python is a high-level programming language known for its readability, simple syntax, and versatility. I chose Python because it is beginner-friendly and provides useful tools for developing practical software applications. During development, I applied functions, conditional statements, loops, exception handling, SQL queries, and database operations. This project has improved my understanding of how Python interacts with databases and strengthened my logical thinking, technical confidence, and problem-solving abilities.

## Useful Websites
The following websites provided helpful learning resources and documentation during the development of this project:
- [Python Official Documentation](https://docs.python.org/3/)
- [SQLite Official Documentation](https://www.sqlite.org/docs.html)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [GeeksforGeeks Python and SQL Tutorials](https://www.geeksforgeeks.org/)
- [freeCodeCamp](https://www.freecodecamp.org/)

## Future Work
Although this application provides basic petroleum logistics and inventory management functionalities, there are several improvements I would like to implement in the future:
1. **User Authentication:** Add login and registration features to ensure that only authorized users can access the system.
2. **Improved User Interface:** Develop a graphical user interface to make the application easier to navigate and use.
3. **Advanced Reporting:** Add more detailed financial reports, delivery summaries, and inventory analysis.
4. **Inventory Alerts:** Introduce automatic notifications when petroleum stock reaches a specified minimum quantity.
5. **Data Validation:** Improve input validation and error handling to prevent incorrect or incomplete records.
6. **Database Backup:** Implement a database backup and recovery feature to protect important business information.
7. **Dashboard and Analytics:** Add a dashboard that displays inventory levels, delivery activities, and financial performance.
8. **Export Reports:** Allow users to export delivery and financial reports into Excel or PDF formats.