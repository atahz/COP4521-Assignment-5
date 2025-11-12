import sqlite3

# connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
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

# commit and save changes to database
conn.commit()

# close the connection
conn.close()