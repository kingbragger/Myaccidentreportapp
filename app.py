# Import necessary modules
from flask import Flask, render_template, request, redirect

# Create Flask app
app = Flask(__name__)

# In-memory storage for accident reports (replace with a database in a real-world scenario)
accident_reports = []

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html', reports=accident_reports)

# Route for submitting a new accident report
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Retrieve form data
        date = request.form['date']
        location = request.form['location']
        description = request.form['description']

        # Create a new accident report
        report = {
            'date': date,
            'location': location,
            'description': description
        }

        # Add the report to the list
        accident_reports.append(report)

        return redirect('/')
    else:
        return "Invalid request method"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
