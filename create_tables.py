import sqlite3

# connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('usersAndContest.db')
cur = conn.cursor()

# create the users table
cur.execute('''CREATE TABLE Users (
            Uid INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Age INTEGER NOT NULL,
            PhoneNumber TEXT NOT NULL,
            SecurityLevel INTEGER NOT NULL,
            LoginPassword TEXT NOT NULL
            )''')

# create the contest table
cur.execute('''CREATE TABLE Contest (
            Eid INTEGER PRIMARY KEY AUTOINCREMENT,
            Uid INTEGER NOT NULL,
            BakingItemName TEXT NOT NULL,
            NumOfExcellentVotes INTEGER NOT NULL,
            NumOfOkVotes INTEGER NOT NULL,
            NumOfBadVotes INTEGER NOT NULL,
            FOREIGN KEY (Uid) REFERENCES Users(Uid)
                ON DELETE CASCADE ON UPDATE CASCADE
            )''')

# commit and save changes to database
conn.commit()

# close the connection
conn.close()