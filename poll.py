from flask import Flask, render_template, request
app = Flask(__name__)
 
poll_data = {
  'question': 'Which course is the worst?',
  'fields': ['Introduction to Programming', 'Systems Management', 'Digital Circuits', 'Math 1: Linear Algebra', 'Communication Skills']
}

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
    if request.method == 'POST':
        field = request.form['field']
        votes[field] += 1
 
    # show results
    return render_template('results.html', data=poll_data, votes=votes)
 
app.run(host="0.0.0.0", debug=True)

#credits: https://code-maven.com/a-polling-station-with-flask
