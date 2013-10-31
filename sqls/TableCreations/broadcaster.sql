DROP TABLE IF EXISTS broadcaster;

CREATE TABLE IF NOT EXISTS broadcaster (
id serial PRIMARY KEY,
name VARCHAR(45),
channel INT,
country VARCHAR(10),
language VARCHAR(5)
);