CREATE DATABASE test;
USE test;

CREATE TABLE `customers`(
    `uuid` VARBINARY(16) DEFAULT (RANDOM_BYTES(16)) NOT NULL PRIMARY KEY,
    `name` VARCHAR(200) NOT NULL,
    `email` VARCHAR(200)NOT NULL,
    `password` varchar(255) default null,
    `age` TINYINT UNSIGNED,
    `address` TEXT DEFAULT NULL
);

CREATE TABLE `products`(
    `id` INT NOT NULL PRIMARY KEY,
    `name` VARCHAR(200) NOT NULL,
    `price` FLOAT(6,2)NOT NULL,
    `total_quantity` INT UNSIGNED NOT NULL,
    `available_quantity` INT UNSIGNED NOT NULL, 
    `holded_quantity` INT UNSIGNED NOT NULL
);

CREATE TABLE `administrators`(
    `uuid` VARBINARY(16) DEFAULT (RANDOM_BYTES(16)) NOT NULL PRIMARY KEY,
    `name` VARCHAR(200) NOT NULL,
    `email` VARCHAR(200)NOT NULL,
    `password` varchar(255) NOT NULL
);

