import sqlite3

# connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('contest.db')
cur = conn.cursor()

# create the contest table
cur.execute('''CREATE TABLE Contest (
            Eid INTEGER PRIMARY KEY AUTOINCREMENT,
            Uid FOREIGN KEY REFERENCES Users(Uid),
            BakingItemName TEXT NOT NULL,
            NumOfExcellentVotes INTEGER NOT NULL,
            NumOfOkVotes INTEGER NOT NULL,
            NumOfBadVotes INTEGER NOT NULL
            )''')

# commit and save changes to database
conn.commit()

# close the connection
conn.close()