

# Fullstack Project 2 - Tournament
Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.
The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

## Files
* tournament.py
* tournament.sql
* tournament_test.py

## Requirements
1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
2. Clone the http://github.com/udacity/fullstack-nanodegree-vm (which include vagrant file)
2. Clone the https://github.com/taro03/tournament
3. Launch the Vagrant VM
4. Run a test suite to verify your code (tournament_test.py)


Expected result
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
