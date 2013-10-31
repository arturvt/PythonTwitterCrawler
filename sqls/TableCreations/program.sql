DROP TABLE IF EXISTS program;

CREATE TABLE IF NOT EXISTS program (
id serial PRIMARY KEY,
name VARCHAR(100),
broadcaster serial references broadcaster(id))
