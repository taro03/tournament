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
CREATE TABLE players (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
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
CREATE TABLE matches (
    id BIGSERIAL PRIMARY KEY,
    winner INTEGER REFERENCES players(player_id) NOT NULL,
    loser INTEGER REFERENCES players(player_id) NOT NULL
);

/*
view standings
view standing will combine the table players and matches to filter out
the player order by the most winning. The next match and the final result
will based on the outcome of this view
*/
CREATE VIEW standings AS
	SELECT players.id, players.name,
	(SELECT count(matches.winner)
		FROM matches
		WHERE players.id=matches.winner OR players.id=matches.loser)
	AS num_win,
	(SELECT count(matches.matchID)
		FROM matches
		WHERE players.id=matches.winner OR players.id=matches.loser)
	AS num_matches
	FROM players
	ORDER BY num_win DESC;

/*
view skip_count to show how many time a player skip a round
*/
CREATE VIEW skip_count AS
	SELECT players.id, players.name, count(matches.winner) AS num_skip
	FROM players LEFT JOIN matches
	ON players.id = matches.winner and matches.loser IS NULL
	GROUP BY players.id;
