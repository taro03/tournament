import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    db = connect('tournament.db')
    c = db.cursor()
    query = "DELETE * FROM matches"
    c.execute(query)
    db.close()

def deletePlayers(db, c):
    """Remove all the player records from the database."""
    db = connect('tournament.db')
    c = db.cursor()
    query = "DELETE * FROM players"
    c.execute(query)
    db.close()

def countPlayers(db, c):
    """Returns the number of players currently registered."""
    db = connect('tournament.db')
    c = db.cursor()
    query = "SELECT playerID as num FROM players"
    c.execute(query)
    count = c.fetchall()[0][0]
    db.close()
    return count


def registerPlayers(playerName):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect('tournament.db')
    c = db.cursor()
    query = """INSERT INTO players(playerName)
               VALUES (%s)"""
    c.execute(query, %playerName)
    db.close()

def playerStandings():
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
    db = connect('tournament.db')
    c = db.cursor()
    query = """SELECT playerID, playerName, numWin, numLoss
               FROM players
               ORDER BY numWin"""
    c.execute(query)
    db.close()
    return c.fetchall()

def reportMatch(winnerID, loserID):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect('tournament.db')
    c = db.cursor()
    query1 = """INSERT INTO matches(winner, loser)
               VALUES (%s, %s)"""
    match_report = (winnerID, loserID)
    c.execute(query1, match_report)
    db.commit()

    query2 = """UPDATE players
               SET numWin += 1
               WHERE playerID= (%s)"""
    match_report = (winnerID)
    c.excute(query2,match_report)
    db.commit()

    query3 = """UPDATE players
               SET numLoss += 1
               WHERE playerID = (%s)"""
    match_report = (loserID)
    c.execute(query3, match_report)
    db.commit()

def swiss_paring():
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
    db = connect('tournament.db')
    c = db.cursor()
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
    db.close()
    return match_pairing
    

    
    
    
    
    
