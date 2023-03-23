DROP TABLE IF EXISTS message;
DROP TABLE IF EXISTS file;
DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS account;
DROP TABLE IF EXISTS role;

CREATE TABLE IF NOT EXISTS role(
    id SERIAL,
    name VARCHAR(50),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS account(
    id SERIAL,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    role_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (role_id) REFERENCES role
);

CREATE TABLE IF NOT EXISTS category(
    id SERIAL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS status(
    id SERIAL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS ticket(
    id SERIAL,
    content VARCHAR(500) NOT NULL,
    date_creation TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    status_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    sender_id INTEGER NOT NULL,
    support_id INTEGER NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (sender_id) REFERENCES account(id) ON DELETE CASCADE,
    FOREIGN KEY (support_id) REFERENCES account(id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES status(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS file(
    id SERIAL,
    link VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS message(
    id SERIAL,
    content VARCHAR(500) NOT NULL,
    date_creation TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    sender_id INTEGER NOT NULL,
    ticket_id INTEGER NOT NULL,
	PRIMARY KEY (id),
    FOREIGN KEY (sender_id) REFERENCES account(id) ON DELETE CASCADE,
    FOREIGN KEY (ticket_id) REFERENCES ticket(id) ON DELETE CASCADE
);
