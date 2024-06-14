from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['feedback']
    
    with open('feedback.csv', 'a', newline='') as csvfile:
        fieldnames = ['name', 'email', 'feedback']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header only if the file is empty
        csvfile.seek(0, 2)  # move to end of file
        if csvfile.tell() == 0:
            writer.writeheader()
        
        writer.writerow({'name': name, 'email': email, 'feedback': feedback})
    
    return redirect('/thank_you')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
