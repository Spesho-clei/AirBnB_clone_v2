-- Check if the database 'hbnb_test_db' exists, if not, create it
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Check if the user 'hbnb_test' exists, if not, create it and set the password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the 'hbnb_test_db' database to the 'hbnb_test' user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the 'performance_schema' database to the 'hbnb_test' user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
