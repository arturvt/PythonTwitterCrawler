DROP TABLE IF EXISTS program;
DROP TABLE IF EXISTS hashtags;
DROP TABLE IF EXISTS associated_context;

CREATE TABLE  program (
	id SERIAL NOT NULL,
	name VARCHAR(100),
	broadcaster_id int4 DEFAULT 0,
	associated_context_id int4 DEFAULT 0,

PRIMARY KEY (id),
UNIQUE(broadcaster_id),
FOREIGN KEY (broadcaster_id) REFERENCES broadcaster(id),
FOREIGN KEY (associated_context_id) REFERENCES associated_context(associated_id)
);

CREATE TABLE associated_context (
        associated_id SERIAL NOT NULL,
        usertwitter VARCHAR(50) DEFAULT '',
        program_id SERIAL DEFAULT 0,

PRIMARY KEY(id),
UNIQUE(program_id),
FOREIGN KEY (program_id) REFERENCES program(id)
);


CREATE TABLE hashtags (
        hash_id SERIAL NOT NULL,
        value VARCHAR(100),
        associated_id SERIAL DEFAULT 0,

PRIMARY KEY(id),
UNIQUE(associated_id),
FOREIGN KEY (associated_id) REFERENCES associated_context
);

