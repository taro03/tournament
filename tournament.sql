/*
### tournaments.sql - schema file for storing tournament data

The database schema is composed of three tables (tournaments, contestants, and
matches) as described below. The database adheres to (at least) 1NF and 5NF for
the following reasons:

1NF - No column stores an array type, so there is no way to insert
multiple values into a column. All columns use foreign keys or automatically
generated serials where possible, and default / NOT NULL constrains elsewhere
to ensure that values can only come from the type's domain.

5NF - No table can be recreated by joining together other tables (without one
of them being the table itself), so there are no join depedencies, and the
database is therefore trivially in 5NF.

Despite being a requirement for a "completely Udacious", I chose not to use
views because none of the queries in the API would be simplified by using a
view - there are no subqueries or compilcated constraints with more than one
WHERE clause.

tournaments
------
Stores information about each tournament.

name (varchar, primary key) - The name of the tournament.

event (varchar) - What sort of event the tournament is for (swimming, chess,
cup-stacking, etc).


contestants
------
Stores information about contestants for each tournament.

id (bigserial, primary key) - The ID number of the contestant. Since
no contestant should be entered into the same tournament twice, it is the
primary key.

name (varchar) - The player's actual human name.

tournament (bigint) - which tournament this contestant is entered in. This
column uses tournaments.name as a foreign key.

wins (bigint) - How many matches this contestant won.

losses (bigint) - How many matches this contestant loss


matches
------
Stores information about matches and their outcomes.

id (bigserial, primary key) - A unique identifier for the match.

tournament (varchar) - which tournament this match was in. This
column uses tournaments.name as a foreign key.

winner (bigint) - The name of the first contestant; a foreign key for
this column is contestants.id

loser (bigint) - The name of the second contestant; a foreign key for
this column is contestants.id

*/
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\connect tournament;

create table players (
    playerID BIGSERIAL PRIMARY KEY,
    playerName VARCHAR NOT NULL,
    
);

create table matches (
    matchID BIGSERIAL PRIMARY KEY,
    winner INTEGER REFERENCES players(playerID) NOT NULL,
    loser INTEGER REFERENCES players(playerID) NOT NULL
);

/*create view standings as
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
	ORDER BY num_win DESC, num_matches DESC;*/

