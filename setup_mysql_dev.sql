-- Check if the database 'hbnb_dev_db' exists, if not, create it
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Check if the user 'hbnb_dev' exists, if not, create it and grant privileges
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the 'hbnb_dev_db' database to the 'hbnb_dev' user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the 'performance_schema' database to the 'hbnb_dev' user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
