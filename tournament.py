import psycopg2

def connect():
    db=psycopg2.connect("dbname = tournament")
    c = db.cursor()
    return db, c

def deleteMatches(db, c):
    query = "DELETE * FROM matches"
    c.execute(query)
    db.commit()
    db.close()

def Players(db, c):
    query = "DELETE * FROM players"
    c.execute(query)
    db.commit()
    db.close

def countPlayers(db, c):
    query = "SELECT playerID as num FROM players"
    c.execute(query)
    num = c.fetchall()[0][0]
    return num


def registerPlayers(db, c, playerID, playerName):
    query = """INSERT INTO players(playerID, playerName)
               VALUE (%s, %s)"""
    c.execute(query %playerID, %playerName)
    db.commit()
    db.close()

def playerStandings(db, c):
    query = """SELECT playerID, playerName, numWin, numLoss
               FROM players
               ORDER BY numWin"""
    c.execute(query)
    db.commit()
    db.close()
    return c.fetchall()

def reportMatch(db, c, winner, loser):
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
    

    
    
    
    
    
