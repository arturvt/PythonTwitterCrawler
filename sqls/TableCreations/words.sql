﻿DROP TABLE IF EXISTS terms;

CREATE TABLE IF NOT EXISTS terms (
id serial PRIMARY KEY,
word VARCHAR(45),
status INT
);