/*
### tournaments.sql - schema file for storing tournament data

The database schema is composed of 2 TABLES (players, match) and
1 VIEW as described below. 
*/

/*create a db and set up a connection to it */
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\connect tournament;

/*
table players
Stores information about players

playerID (bigserial, primary key) - The ID number of the players. Since
	no contestant should be entered into the same tournament twice, it is the
	primary key.
playerName (varchar) - The player's actual human name.
*/
create table players (
    playerID BIGSERIAL PRIMARY KEY NOT NULL,
    playerName VARCHAR NOT NULL,
);

/*
table matches
Stores information about matches and their outcomes.

matchID (bigserial, primary key) - A unique identifier for the match.
winner (integer) - The name of the first player; a foreign key for
	this column is players.playerID
loser (intefer) - The name of the second player; a foreign key for
	this column is players.playername
*/
create table matches (
    matchID BIGSERIAL PRIMARY KEY,
    winner INTEGER REFERENCES players(playerID) NOT NULL,
    loser INTEGER REFERENCES players(playerID) NOT NULL
);

/*
view standings
view standing will combine the table players and matches to filter out
the player order by the most winning. The next match and the final result
will based on the outcome of this view
*/
create view standings as
	SELECT players.playerID, players.playerName,
	(SELECT count(matches.winner)
		FROM matches
		WHERE players.playerID=matches.winner)
	AS num_win,
	(SELECT count(matches.matchID)
		FROM matches
		WHERE players.playerID=matches.loser)
	AS num_matches
	FROM players
	ORDER BY num_win DESC;

