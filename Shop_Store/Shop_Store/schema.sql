DROP TABLE IF EXISTS shop;

CREATE TABLE shop
(
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    amount_sold INTEGER NOT NULL,
    stock INTEGER NOT NULL
);

INSERT INTO shop (name, amount_sold, stock)
VALUES 
    ('Sea Bass', 0, 50),
    ('Salmon', 0, 50),
    ('Cod', 0, 50),
    ('Halibut', 0, 50),
    ('Haddock', 0, 50),
    ('Beef Burger', 0, 50),
    ('Chicken Burger', 0, 50),
    ('Chips', 0, 150),
    ('Chicken Wings', 0, 80),
    ('Burger Buns', 0, 300);


DROP TABLE IF EXISTS employees;

CREATE TABLE employees
(
    employee_id INTEGER PRIMARY key AUTOINCREMENT,
    first_name TEXT NOT NULL,
    surname TEXT NOT NULL,
    work_days TEXT NOT NULL
);

INSERT INTO employees (first_name, surname, work_days)
VALUES 
    ("Eoin", "Murphy", "Monday, Tuesday, Wednesday"),
    ("Kerstin", "Förstner", "Tuesday, Wednesday, Thursday"),
    ("Arno", "Jahn", "Wednesday, Thursady, Friday"),
    ("Marius", "Bergmann", "Thrusday, Friday, Saturday"),
    ("Evan", "Scott", "Friday, Saturyday");