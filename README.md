

# Fullstack Project 2 - Tournament
Description: Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.
The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

Full instruction [here](https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true)

## Files
* tournament.py
* tournament.sql
* tournament_test.py

## Requirements
1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
2. Clone the http://github.com/udacity/fullstack-nanodegree-vm (which include vagrant file)
2. Clone the https://github.com/taro03/tournament
3. Launch the Vagrant VM
4. Connect psql to your new database and create tables from the statements written in ```tournament.sql```:
a.Paste each statement in to psql
b.Use the command ```\i tournament.sql``` to import the whole file into psql at once.
5. Run ```python [path]]tournament_test.py``` to verify


##Expected result
```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py 
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```
