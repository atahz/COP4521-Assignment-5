from flask import Flask, render_template
app = Flask(__name__)

# if the user goes to the root URL, 
# http://127.0.0.1:5000/
# display the home page
@app.route('/')
def Home():
    # display links to other pages
    # use an unordered list with no bullet points,
    # no padding, and no margin, for no indentation
    return '''
    <ul style="list-style-type: none; padding: 0; margin: 0;">
        <li><a href="/enternew">Add new Baking Contest User</a></li>
        <li><a href="/list">List Baking Contest Users</a></li>
        <li><a href="/contestResults">Baking Contest Entry Results</a></li>
    </ul>
    '''

# if the user goes to the enternew URL, 
# http://127.0.0.1:5000/enternew
# display the Add New Baking Contest User page

# make sure to have a http://127.0.0.1:5000/addrec
# page with validation error messages

# if the user goes to the list URL, 
# http://127.0.0.1:5000/list
# display the List Baking Contest Users page
@app.route('/list')
def UsersList():
    import sqlite3

    # connect to the database
    conn = sqlite3.connect('usersAndContest.db')
    cur = conn.cursor()

    # get users' info from the Users table
    cur.execute('SELECT Name, Age, PhoneNumber, SecurityLevel, LoginPassword FROM Users')
    usersInfo = cur.fetchall()

    # close the connection
    conn.close()

    # render the usersList.html template
    return render_template('usersList.html', tableData = usersInfo)

# if the user goes to the contestResults URL, 
# http://127.0.0.1:5000/contestResults
# display the Baking Contest Entry Results page
@app.route('/contestResults')
def ContestResults():
    import sqlite3

    # connect to the database
    conn = sqlite3.connect('usersAndContest.db')
    cur = conn.cursor()

    # get contest results from the Contest table
    cur.execute('SELECT * FROM Contest')
    contestResults = cur.fetchall()

    # close the connection
    conn.close()

    # render the contestResults.html template
    return render_template('contestResults.html', tableData = contestResults)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)