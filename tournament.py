import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    db=psycopg2.connect("dbname = tournament")
    c = db.cursor()
    return db, c

def deleteMatches(db, c):
    """Remove all the match records from the database."""
    query = "DELETE * FROM matches"
    c.execute(query)
    db.commit()
    db.close()

def deletePlayers(db, c):
    """Remove all the player records from the database."""
    query = "DELETE * FROM players"
    c.execute(query)
    db.commit()
    db.close

def countPlayers(db, c):
    """Returns the number of players currently registered."""
    query = "SELECT playerID as num FROM players"
    c.execute(query)
    num = c.fetchall()[0][0]
    return num


def registerPlayers(db, c, playerID, playerName):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    query = """INSERT INTO players(playerID, playerName)
               VALUE (%s, %s)"""
    c.execute(query %playerID, %playerName)
    db.commit()
    db.close()

def playerStandings(db, c):
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    query = """SELECT playerID, playerName, numWin, numLoss
               FROM players
               ORDER BY numWin"""
    c.execute(query)
    db.commit()
    db.close()
    return c.fetchall()

def reportMatch(db, c, winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query = """INSERT INTO matches(winner, loser)
               VALUES (%s, %s)"""
    match_report = (winner, loser)
    c.execute(query, match_report)
    db.commit()

    query = """UPDATE players
               SET wins += 1
               WHERE playerID= (%s)"""
    match_report = (winner)
    c.excute(query,match_report)
    db.commit()

    query = """UPDATE players
               SET losses += 1
               WHERE playerID = (%s)"""
    match_report = (loser)
    c.execute(query, loser)
    db.commit()

def swiss_paring(db, c):
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
    match_paring=[]
    query = """SELECT playerID, playerName
               FROM players
               ORDER BY numWin desc"""
    c.execute(query)
    2rows = c.fetchmany(2)
    while 2rows:
        pair=[]
        for row in 2rows:
             pair += list(row)
        match_pairing.append(pair)
        2rows = c.fetchmany(2)
    return match_pairing
    

    
    
    
    
    
