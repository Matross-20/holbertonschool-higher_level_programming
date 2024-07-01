-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;

-- Use the database
USE hbtn_0e_6_usa;

-- Create the states table
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

