from flask import Flask
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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)