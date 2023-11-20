-- script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- SET GLOBAL validate_password.policy = 'LOW';
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- give priviliges to the MySQL server user hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- SET GLOBAL validate_password.policy = 'MEDIUM';

FLUSH PRIVILEGES;
