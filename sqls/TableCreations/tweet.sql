DROP TABLE IF EXISTS tweets;

CREATE TABLE IF NOT EXISTS tweets (
id serial PRIMARY KEY,
datecreation timestamp  without time zone ,
geolocation VARCHAR(40),
key_word VARCHAR(25),
post VARCHAR(210)
);