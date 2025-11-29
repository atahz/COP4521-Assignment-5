import sqlite3

def create_tables():
    # connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('usersAndContest.db')
    cur = conn.cursor()

    # drop existing tables
    cur.execute('DROP TABLE IF EXISTS Users')
    cur.execute('DROP TABLE IF EXISTS Contest')

    try:
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

        # initialize tables with default data after creation
        init_tables()

    except sqlite3.OperationalError:
        pass

    # close the connection
    conn.close()

def init_tables():
    # connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('usersAndContest.db')
    cur = conn.cursor()

    try:
        # execute multiple commands to populate the users table
        cur.executescript('''INSERT INTO Users (Name, Age, PhoneNumber, SecurityLevel, LoginPassword)
                            VALUES ('Hayley Williams', 36, '555-111-2222', 1, 'test123');
                            INSERT INTO Users (Name, Age, PhoneNumber, SecurityLevel, LoginPassword)
                            VALUES ('Chris Isaak', 69, '555-222-3333', 2, 'test456');
                            INSERT INTO Users (Name, Age, PhoneNumber, SecurityLevel, LoginPassword)
                            VALUES ('Lana del Rey', 40, '555-333-4444', 3, 'test789');''')

        # execute multiple commands to populate the contest table
        cur.executescript('''INSERT INTO Contest (Uid, BakingItemName, NumOfExcellentVotes, NumOfOkVotes, NumOfBadVotes)
                            VALUES (1, 'Chocolate Chip Cookies', 9, 3, 3);
                            INSERT INTO Contest (Uid, BakingItemName, NumOfExcellentVotes, NumOfOkVotes, NumOfBadVotes)
                            VALUES (2, 'Brownies', 7, 4, 4);
                            INSERT INTO Contest (Uid, BakingItemName, NumOfExcellentVotes, NumOfOkVotes, NumOfBadVotes)
                            VALUES (3, 'Banana Bread', 11, 2, 2);''')

        # commit and save changes to database
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    # close the connection
    conn.close()

def insert_user(name, age, phone, security, password):
    # connect to the database
    conn = sqlite3.connect('usersAndContest.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO Users (Name, Age, PhoneNumber, SecurityLevel, LoginPassword) VALUES (?, ?, ?, ?, ?)",
                (name, age, phone, security, password))
    conn.commit()
    conn.close()

def insert_contest_item(username, name, excellentVotes, okVotes, badVotes):
    # connect to the database
    conn = sqlite3.connect('usersAndContest.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    #get the user uid for foreign key
    uid = cur.execute("SELECT Uid FROM Users WHERE Name = ?", (username,)).fetchone()
    uid = uid['Uid']
    if uid:
        cur.execute("INSERT INTO Contest (Uid, BakingItemName, NumOfExcellentVotes, NumOfOkVotes, NumOfBadVotes) VALUES (?, ?, ?, ?, ?)",
                    (uid, name, excellentVotes, okVotes, badVotes))
    conn.commit()
    conn.close()