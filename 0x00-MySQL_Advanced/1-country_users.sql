-- Create a table users

CREATE TABLE IF NOT EXISTS users (
    -- ID declaration
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- User email
    email VARCHAR(255) NOT NULL UNIQUE,

    -- User's name
    name VARCHAR(255)

    -- Countries enumeration
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);