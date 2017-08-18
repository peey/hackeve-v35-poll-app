# credits: adapted from https://code-maven.com/a-polling-station-with-flask
from flask import Flask, render_template, request
app = Flask(__name__)
 
poll_data = {
  'question': 'Which course is the worst?',
  'fields': ['Introduction to Programming', 'Systems Management', 'Digital Circuits', 'Math 1: Linear Algebra', 'Communication Skills']
}

def save(obj, filename):
    """
    This function takes an object, converts it to JSON string representation and saves it to
    the provided filename
    """
    import json
    string = json.dumps(obj)

    with open(filename, 'w') as file:
        file.write(string)

def load(filename):
    """
    This function loads the data saved by the save function
    """
    import json
    file = open(filename, 'r')
    return json.loads(file.read())


try:
    # if the file exists
    votes = load('vote_data.json') 
except:
    # if the file does not exist
    votes = {}
    # initialize
    for f in poll_data['fields']:
        votes[f] = 0
 
@app.route('/')
def root():
    # show poll on the landing page
    return render_template('poll.html', data=poll_data)
 
@app.route('/results', methods=['GET', 'POST'])
def poll():
    """
    To learn more about getting data from forms, try these links: 
      http://opentechschool.github.io/python-flask/core/form-submission.html
      http://opentechschool.github.io/python-flask/core/forms.html
    """
    if request.method == 'POST': # if we've gotten data from the form
        field = request.form.get('field')
        votes[field] += 1
        save(votes, 'vote_data.json')
 
    # show results
    return render_template('results.html', data=poll_data, votes=votes)

# host 0.0.0.0 allows anyone with your IP to access the running app.
# you can access it by going to 127.0.0.1:5000 and others can access it by your ip:5000
# you can find your local IP by using command `hostname -I` on linux / mac, or 
# using ipconfig in cmd for windows (see https://www.groovypost.com/wp-content/uploads/2009/10/image_417.png)
app.run(host="0.0.0.0", debug=True) 
