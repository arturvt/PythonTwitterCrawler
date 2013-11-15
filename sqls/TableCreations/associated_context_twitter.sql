DROP TABLE IF EXISTS associated_context_twitter;

CREATE TABLE IF NOT EXISTS associated_context_twitter (
id serial PRIMARY KEY,
usertwitter VARCHAR(45),
program serial references program(id));

