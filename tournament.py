#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except:
        print ("Could not connect to the database")

def deleteMatches():
    """Remove all the match records from the database."""
    db, c = connect()
    query = "DELETE FROM matches;"
    c.execute(query)
    query1 = "DELETE FROM players;"
    c.execute(query1)
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db, c = connect()
    query = "DELETE FROM players"
    c.execute(query)
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db,c = connect()
    query = "SELECT count(id) as player_count FROM players"
    c.execute(query)
    player_count = c.fetchone()[0]
    db.close()
    return player_count

def registerPlayer(playerName):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    db,c = connect()
    query = """INSERT INTO players(name)
               VALUES (%s)"""
    parameter = (name,)
    c.execute(query, parameter)
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, c = connect()
    query = """SELECT * FROM standings;"""
    c.execute(query)
    matches = c.fetchall()
    db.close()
    return matches

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, c = connect()
    query = """INSERT INTO matches(winner, loser)
               VALUES (%s, %s)"""
    parameter = (winner, loser,)
    c.execute(query, parameter)
    db.commit()
    db.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    playerStandings()
    match_pairing = []
    count = len(matches)
    for i in range(0, count-1, 2):
        pairs = (matches[i][0], matches[i][1], matches[i+1][0], matches[i+1][1])
        match_pairing.append(pairs)
    return match_pairing
    db.close()
    #!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except:
        print ("Could not connect to the database")

def deleteMatches():
    """Remove all the match records from the database."""
    db, c = connect()
    query = "DELETE FROM matches;"
    c.execute(query)
    query1 = "DELETE FROM players;"
    c.execute(query1)
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db, c = connect()
    query = "DELETE FROM players"
    c.execute(query)
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db,c = connect()
    query = "SELECT count(id) as player_count FROM players"
    c.execute(query)
    player_count = c.fetchone()[0]
    db.close()
    return player_count

def registerPlayer(playerName):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    db,c = connect()
    query = """INSERT INTO players(name)
               VALUES (%s)"""
    parameter = (name,)
    c.execute(query, parameter)
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, c = connect()
    query = """SELECT * FROM standings;"""
    c.execute(query)
    matches = c.fetchall()
    db.close()
    return matches

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, c = connect()
    query = """INSERT INTO matches(winner, loser)
               VALUES (%s, %s)"""
    parameter = (winner, loser,)
    c.execute(query, parameter)
    db.commit()
    db.close()

def skipRound():
    """Assign a player who has yet to skip a round
    return a player(id, name) who is assigned to skip this round
    """
    db, c = connect()
    query = "SELECT id, name FROM skip_count WHERE num_skip = 0 LIMIT 1;"
    c.execute(query)
    player_skipped = c.fetchone()
    db.close()
    return players_skipped

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    match_pairing = []
    skipPlayer = False
    skipPair = False

    # get players standing from playerStandings function
    standings = playerStandings()
    num_players = len(standings)

    if (num_players % 2) !=0:
        # if there are odd players, a player will be skipped each round
        skipPlayer = skipRound()

        i=0
        while i < num_players:
            if skipPlayer:
                # If first player is skipped, create a skipped pair
                # and pairing the next two
                if skipPlayer[0] == standings[i][0]:
                    skipPair = (standings[i][0], standings[i][1],'',"skip")
                    i += 1
                    continue
                # If second player is skipped, pairing the first and the third
                # player, create skipped pair for second player
                elif skipPlayer[0] == standings[i+1][0]:
                    pair = (standings[i][0], standings[i][1], standings[i+2][0], standings[I=2][1])

                    skipPair = (standings[i+1][0],standings[i+1][1],'',"skip")
                    i += 3
    else:
    # if there are even players, just pairing two player
        pair = (
            standings[i][0],
            standings[i][1],
            standings[i+1][0],
            standings[i+1][1]
        )
        i += 2

    match_pairing.append(pair)
    # if a player with skipped round exist
    if skipPair:
        match_pairing.append(skipPair)

    tuple(match_pairing)
    return match_pairing
