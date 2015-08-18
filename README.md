

# Fullstack Project 2 - Tournament
Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.
The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

## Files
* tournament.py
* tournament.sql
* tournament_test.py

## Requirements
You will need to have vagrant and virtual box installed, for instructions on vagrant go to [install vagrant](https://www.vagrantup.com/) for instruction on virtual box go to [install virtual box](https://www.virtualbox.org/).
You will also need [postresql](https://wiki.postgresql.org/wiki/Detailed_installation_guides) and [psycopg2](https://pypi.python.org/pypi/psycopg2)
1. Install Vagrant and VirtualBox
Clone the fullstack-nanodegree-vm repository
Launch the Vagrant VM
Write SQL database and table definitions in a file (tournament.sql)
Write Python functions filling out a template of an API (tournament.py)
Run a test suite to verify your code (tournament_test.py)

## Steps

1. Launch virtual box
2. cd to this repo
3. Launch vagrant ``` vagrant up```
4. Log into vagrant ``` vagrant ssh```
5. CD to the corresponding directory ``` cd /vagrant/tournament ```
6. Prep commandline to insert queries ``` psql```
7. Insert the tables ``` \i tournament.sql```
8. Exit psql ``` \q ```
9. Run the tests ``` python tournament_test.py```

You should see the following output <br>
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
