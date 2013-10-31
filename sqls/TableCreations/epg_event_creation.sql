DROP TABLE IF EXISTS epg_event;

CREATE TABLE IF NOT EXISTS epg_event (
id serial PRIMARY KEY,
descriptor VARCHAR(500),
startDate VARCHAR(10),
startTime VARCHAR(10),
durationTime VARCHAR(10),
program serial references program(id))