CREATE DATABASE tournamentdb;

\connect tournamentdb;

CREATE TABLE tournaments (
    name VARCHAR PRIMARY KEY NOT NULL,
    event VARCHAR NOT NULL
);

create table contestants (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    tournament VARCHAR REFERENCES tournaments(name),
    wins BIGINT NOT NULL DEFAULT 0,
    losses BIGINT NOT NULL DEFAULT 0
);

create table matches (
    id BIGSERIAL PRIMARY KEY,
    tournament VARCHAR REFERENCES tournaments(name),
    winner BIGINT REFERENCES contestants(id),
    loser BIGINT REFERENCES contestants(id)
);
