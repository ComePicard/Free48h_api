INSERT INTO category(name)
VALUES('Matériel'),('Connection'),('Autre');

INSERT INTO role(name)
VALUES('Utilisateur'), ('Support');

INSERT INTO status(name)
VALUES('En attente'), ('Répondu'), ('En cours');

INSERT INTO account(firstname, lastname, email, password, role_id)
VALUES('John', 'Doe', 'johndoe@mail.com', 'johndoe123', 1), ('Alan', 'Poe', 'alanpoe@mail.com', 'alanpoe456', 2);

INSERT INTO ticket(content, sender_id, category_id, status_id)
VALUES ('Message de test pour le ticket 1', 1, 1, 1), ('Message de test pour le ticket 2', 2, 2, 2);

INSERT INTO file(link, ticket_id)
VALUES ('http://img.png', 1), ('http://sanic.png', 1);

INSERT INTO message(content, sender_id, ticket_id)
VALUES ('Message lié au ticket 1', 1, 1), ('Message lié au ticket 2', 2, 2);