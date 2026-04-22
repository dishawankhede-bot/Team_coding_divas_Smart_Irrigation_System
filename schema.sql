CREATE DATABASE IF NOT EXISTS smart_irrigation_db;
USE smart_irrigation_db;

CREATE TABLE IF NOT EXISTS moisture_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sensor_id VARCHAR(50),
    moisture_value INT,
    weather VARCHAR(50),
    pump_status VARCHAR(10),
    tank_level INT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS sensors (
    sensor_id VARCHAR(50) PRIMARY KEY,
    location VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS system_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT IGNORE INTO sensors (sensor_id, location) VALUES
('Sensor1', 'Field A - North'),
('Sensor2', 'Field B - South'),
('Sensor3', 'Field C - East');
