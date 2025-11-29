from flask import Flask, render_template, request, session, jsonify
import tables_mods as db
import errorHandler as err
import sqlite3
import os
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def DoLogin():
    try: 
        user = request.form['username']
        pwd = request.form['password']

        with sqlite3.connect("usersAndContest.db") as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()

            #sends a query to the database to check for user credentials
            sql_select_query = """SELECT * FROM Users WHERE Name = ? AND LoginPassword = ?"""
            row = cur.execute(sql_select_query, (user,pwd)).fetchone()

            if (row != None):
                session['logged_in'] = True
                session['name'] = user
                if int(row['SecurityLevel']) == 1:
                    session['admin'] = True
                else:
                    session['admin'] = False
                return Home()
            else:
                session['logged_in'] = False
                return render_template('login.html', error="invalid username and/or password!")
    except Exception as e:
        con.rollback()
        #flash("error in insert operation")
        #return render_template('login.html', error=f"Login error: {e}")
        
@app.route("/logout")
def logout():
   session['logged_in'] = False
   session['admin'] = False
   session['name'] = ""
   return render_template('login.html')

# if the user goes to the root URL, 
# http://127.0.0.1:5000/
# display the home page
@app.route('/')
def Home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # display links to other pages
        # use an unordered list with no bullet points,
        # no padding, and no margin, for no indentation
        return render_template('home.html', name=session['name'])

# if the user goes to the enternew URL, 
# http://127.0.0.1:5000/enternew
# display the Add New Baking Contest User page
@app.route('/enternew')
def NewUser():
    return render_template('addNewUser.html')

# if the user goes to the enternew URL, 
# http://127.0.0.1:5000/enternew
# display the Add New Baking Contest Item page
@app.route('/enternewItem')
def NewContestItem():
    return render_template('addContestEntry.html')


# make sure to have a http://127.0.0.1:5000/addrec
# page with validation error messages
@app.route('/addrec', methods=['GET', 'POST'])
def AddRec():
    source = request.form.get('source', '')

    if request.method == 'POST' and source == 'addNewUser':
        name = request.form.get('Name', '').strip()
        age = request.form.get('Age', '')
        phone = request.form.get('Phone', '').strip()
        security = request.form.get('Security', '')
        password = request.form.get('Password', '')
        
        errorList = err.UserErrorHandler(name, age, phone, security, password)
        
        # If there are errors, return to form with errors
        if errorList:
            return render_template('addRec.html', errors=errorList)
        
        # If no errors, insert the user into the database
        db.insert_user(name, age, phone, security, password)
        return render_template('addRec.html')  # or redirect

    elif request.method == 'POST' and source == 'addContestEntry':
        name = request.form.get('Name', '').strip()
        excellentVotes = request.form.get('ExcellentVotes', '')
        okVotes = request.form.get('OkVotes', '')
        badVotes = request.form.get('BadVotes', '')

        errorList = err.ContestEntryErrorHandler(name, excellentVotes, okVotes, badVotes)

        if errorList:
            return render_template('addRec.html', errors=errorList)
        
        # If no errors, insert the user into the database
        db.insert_contest_item(session['name'], name, excellentVotes, okVotes, badVotes)
        return render_template('addRec.html')  # or redirect

    else:  # GET request
        return render_template('addRec.html', errors=[])

# if the user goes to the list URL, 
# http://127.0.0.1:5000/list
# display the List Baking Contest Users page
@app.route('/list')
def UsersList():

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

# if the user goes to the myContestResults URL, 
# http://127.0.0.1:5000/myContestResults
# display the Baking Contest Entry Results page
@app.route('/myContestResults')
def MyContestResults():
    # connect to the database
    conn = sqlite3.connect('usersAndContest.db')
    cur = conn.cursor()

    # get contest results from the Contest table
    cur.execute('SELECT BakingItemName, NumOfExcellentVotes, NumOfOkVotes, NumOfBadVotes FROM Contest WHERE Uid = (SELECT Uid FROM Users WHERE Name = ?)', (session['name'],))
    myContestResults = cur.fetchall()

    # close the connection
    conn.close()

    # render the myContestResults.html template
    return render_template('myContestResults.html', tableData = myContestResults)

if __name__ == '__main__':
    db.create_tables()
    #for testing
    app.secret_key = os.urandom(12)
    app.run(host='127.0.0.1', port='5000', debug=True)