CREATE TABLE sensor_data (id SERIAL PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, temperature FLOAT, humidity FLOAT);

insert into sensor_data (temperature, humidity) values (25.5, 60.0);

