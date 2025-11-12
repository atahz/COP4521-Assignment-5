import sqlite3

# connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('contest.db')
cur = conn.cursor()

# execute multiple commands to populate the table
cur.executescript('''INSERT INTO Contest (Uid, BakingItemName, NumOfExcellentVotes, NumOfOkVotes, NumOfBadVotes)
                    VALUES (1, 'Chocolate Chip Cookies', 9, 3, 3);
                    INSERT INTO Contest (Uid, BakingItemName, NumOfExcellentVotes, NumOfOk
                    VALUES (2, 'Brownies', 7, 4, 4);
                    INSERT INTO Contest (Uid, BakingItemName, NumOfExcellentVotes, NumOfOk
                    VALUES (3, 'Banana Bread', 11, 2, 2);''')

# commit and save changes to database
conn.commit()

# close the connection
conn.close()