from app import app
from flask import jsonify

# The route() decorator for the home page
@app.route('/')
@app.route('/index')

# The function that returns the home page message
def index():
    return 'Welcome to the home page!'

# The route() decorator for the user page
@app.route('/profile/<username>', methods=['GET', 'POST'])
def user(username):
    return 'Welcome, {}!'.format(username)

# The route() decorator for the post page
@app.route('/post/<int:post_id>', methods=['GET'])
def post(post_id):
    return 'You are viewing a post with id {}'.format(post_id)

# The route() decorator for JSON data
@app.route('/json', methods=['GET'])
def json_data():
    data = {
        'name': 'Stephen Mangai',
        'course': 'Backend Development with Python',
        'track': 'Python',
        'message': 'I love this course!',
        'company': 'Tunga Academy'
    }
    return jsonify(data)