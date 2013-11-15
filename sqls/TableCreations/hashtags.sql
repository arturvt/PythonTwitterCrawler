DROP TABLE IF EXISTS hashtags;

CREATE TABLE IF NOT EXISTS hashtags (
id serial PRIMARY KEY,
value VARCHAR(60),
associated_context_twitter serial references associated_context_twitter(id));