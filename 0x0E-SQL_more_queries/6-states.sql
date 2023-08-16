-- Creates the db hbtn_0d_usa and the tab states on MySQL server
-- creating hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- using hbtn_0d_usa
USE hbtn_0d_usa;
-- creating states
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256), PRIMARY KEY(id));
