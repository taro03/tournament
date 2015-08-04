CREATE DATABASE tournament;

\connect tournament;

create table players (
    playerID BIGSERIAL PRIMARY KEY,
    playerName VARCHAR NOT NULL,
    numWin BIGINT NOT NULL DEFAULT 0,
    numLoss BIGINT NOT NULL DEFAULT 0
);

create table matches (
    matchID BIGSERIAL PRIMARY KEY,
    winnerID BIGINT REFERENCES players(playerID),
    loserD BIGINT REFERENCES players(playerID)
);
