import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "buildingbharat-dev-key")

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vision')
def vision():
    return render_template('vision.html')

@app.route('/what-we-do')
def what_we_do():
    return render_template('what_we_do.html')

@app.route('/why-building-bharat')
def why_building_bharat():
    return render_template('why_building_bharat.html')

@app.route('/who-we-work-with')
def who_we_work_with():
    return render_template('who_we_work_with.html')

@app.route('/future-goals')
def future_goals():
    return render_template('future_goals.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        organization = request.form.get('organization')
        interests = request.form.get('interests')
        message = request.form.get('message')
        
        # In a real application, this would save to a database or send an email
        # For now, we'll just log the information and flash a message
        logging.info(f"Contact form submission: {name}, {email}, {organization}, {interests}, {message}")
        
        flash('Thank you for reaching out! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
