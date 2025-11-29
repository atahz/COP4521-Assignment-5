from flask import Flask, render_template, request
import tables_mods as db
import sqlite3
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
@app.route('/enternew')
def NewUser():
    return render_template('addNewUser.html')

# make sure to have a http://127.0.0.1:5000/addrec
# page with validation error messages
@app.route('/addrec', methods=['GET', 'POST'])
def AddRec():
    if request.method == 'POST':
        name = request.form.get('Name', '').strip()
        age = request.form.get('Age', '')
        phone = request.form.get('Phone', '').strip()
        security = request.form.get('Security', '')
        password = request.form.get('Password', '')
        
        errorList = []
        
        # Name validation
        if not name or len(name) < 1 or name.isspace():
            errorList.append("You can not enter in an empty name")

        # Phone validation
        if not phone or len(phone) < 1 or phone.isspace():
            errorList.append("You can not enter in an empty phone number")
        
        # Age validation
        try:
            age_int = int(age)
            if age_int <= 0 or age_int > 121:
                errorList.append("The Age must be a whole number greater than 0 and less than 121")
        except (ValueError, TypeError):
            errorList.append("The Age must be a whole number greater than 0 and less than 121")
        
        # Security validation
        try:
            security_int = int(security)
            if security_int < 1 or security_int > 3:
                errorList.append("The SecurityLevel must be a numeric between 1 and 3")
        except (ValueError, TypeError):
            errorList.append("The SecurityLevel must be a numeric between 1 and 3")
        
        # Password validation
        if not password or len(password) < 1 or password.isspace():
            errorList.append("You can not enter in an empty pwd")
        
        # If there are errors, return to form with errors
        if errorList:
            return render_template('addRec.html', errors=errorList)
        
        # If no errors, insert the user into the database
        db.insert_user(name, age, phone, security, password)
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

if __name__ == '__main__':
    db.create_tables()
    app.run()