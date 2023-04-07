CREATE DATABASE test;
USE test;

CREATE TABLE customers(
    CustomerUUID VARBINARY(16) DEFAULT (RANDOM_BYTES(16)) NOT NULL PRIMARY KEY,
    CustomerName VARCHAR(200) NOT NULL,
    Email VARCHAR(200)NOT NULL,
    CustomerPassword varchar(255) NOT NULL,
    Age TINYINT UNSIGNED,
    CustomerAddress TEXT DEFAULT NULL,
)

CREATE TABLE products(
    ProductID int NOT NULL PRIMARY KEY,
    ProductName VARCHAR(200) NOT NULL,
    Price FLOAT(6,2)NOT NULL,
    TotalQuantity INT UNSIGNED NOT NULL,
    AvailableQuantity INT UNSIGNED NOT NULL, 
    HoldedQuantity INT UNSIGNED NOT NULL,
)

CREATE TABLE administrators(
    AdminUUID VARBINARY(16) DEFAULT (RANDOM_BYTES(16)) NOT NULL PRIMARY KEY,
    AdminName VARCHAR(200) NOT NULL,
    Email VARCHAR(200)NOT NULL,
    AdminPassword varchar(255) NOT NULL,
)


INSERT INTO customers (`name`,`email`,`address`,`pan`,`cvv`)
VALUES
  ("Aretha Ward","ut.sagittis@outlook.couk","5658 Nec, Rd.","4913 3175 4987 6633","176"),
  ("Candace Hansen","tempor.erat@google.couk","P.O. Box 921, 3235 Nullam Rd.","453958 194672 7814","119"),
  ("Karina Mcguire","imperdiet.ornare.in@protonmail.net","Ap #404-7736 Nibh. Road","3687 344758 77398","449"),
  ("Cathleen Hughes","nec.urna@icloud.ca","P.O. Box 208, 9218 Sagittis Av.","559623 836666 3165","501"),
  ("Graiden Mcknight","montes@outlook.org","791-2997 Gravida Av.","490327 2449252926","324");