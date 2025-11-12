import sqlite3

# connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
cur = conn.cursor()

# execute multiple commands to populate the table
cur.executescript('''INSERT INTO Users (Name, Age, PhoneNumber, SecurityLevel, LoginPassword)
                    VALUES ('Hayley Williams', 36, '555-111-2222', 1, 'test123');
                    INSERT INTO Users (Name, Age, PhoneNumber, SecurityLevel, LoginPassword)
                    VALUES ('Chris Isaak', 69, '555-222-3333', 2, 'test456');
                    INSERT INTO Users (Name, Age, PhoneNumber, SecurityLevel, LoginPassword)
                    VALUES ('Lana del Rey', 40, '555-333-4444', 3, 'test789');''')

# commit and save changes to database
conn.commit()

# close the connection
conn.close()