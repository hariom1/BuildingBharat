import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "buildingbharat-dev-key")

# Sample course data - In a real application, this would come from a database
courses = {
    'field-operations': {
        'id': 'field-operations',
        'title': 'Political Field Operations Mastery',
        'category': 'Campaign Operations',
        'price': 6999,
        'instructor': 'Rajiv Mehta',
        'duration': '12 hours',
        'level': 'Intermediate',
        'description': 'Master the art of field operations for political campaigns. Learn how to build and manage ground teams, volunteer coordination, canvassing strategies, and voter outreach programs.',
        'image': 'field-operations.jpg',
        'topics': [
            'Volunteer Recruitment & Management',
            'Door-to-Door Canvassing Strategies',
            'Event Organization & Management',
            'GOTV (Get Out The Vote) Operations',
            'Constituency Mapping & Targeting'
        ],
        'demo_video': 'field-operations-demo.mp4',
        'what_you_learn': [
            'Build and manage high-performing volunteer teams',
            'Develop targeted constituency outreach programs',
            'Design and execute effective GOTV operations',
            'Coordinate field activities with central campaign strategy',
            'Utilize technology for field team coordination'
        ]
    },
    'political-research': {
        'id': 'political-research',
        'title': 'Political Research & Analysis',
        'category': 'Research & Insights',
        'price': 5499,
        'instructor': 'Dr. Priya Sharma',
        'duration': '10 hours',
        'level': 'Advanced',
        'description': 'Develop expertise in political research methodologies, policy analysis, and using data to inform campaign strategy and governance approaches.',
        'image': 'political-research.jpg',
        'topics': [
            'Research Methodology for Political Campaigns',
            'Opposition Research Techniques',
            'Public Opinion Analysis',
            'Policy Research & Development',
            'Research-Based Messaging'
        ],
        'demo_video': 'political-research-demo.mp4',
        'what_you_learn': [
            'Conduct rigorous political and policy research',
            'Analyze voting patterns and electoral data',
            'Develop evidence-based policy positions',
            'Create research-backed campaign messaging',
            'Identify and counter opposition narratives'
        ]
    },
    'data-analytics': {
        'id': 'data-analytics',
        'title': 'Political Data Analytics',
        'category': 'Data & Technology',
        'price': 7999,
        'instructor': 'Arjun Patel',
        'duration': '15 hours',
        'level': 'Intermediate to Advanced',
        'description': 'Learn how to leverage data analytics for political campaigns, from voter targeting to resource allocation and performance measurement.',
        'image': 'data-analytics.jpg',
        'topics': [
            'Voter Database Management',
            'Predictive Modeling for Campaigns',
            'Geographic Information Systems (GIS)',
            'A/B Testing for Political Messaging',
            'Performance Analytics & Reporting'
        ],
        'demo_video': 'data-analytics-demo.mp4',
        'what_you_learn': [
            'Build and manage comprehensive voter databases',
            'Develop predictive models for voter turnout and support',
            'Create targeted campaign strategies based on data insights',
            'Implement A/B testing for campaign communications',
            'Measure and optimize campaign performance metrics'
        ]
    },
    'digital-communication': {
        'id': 'digital-communication',
        'title': 'Digital Communication & Media Strategy',
        'category': 'Communication',
        'price': 4999,
        'instructor': 'Neha Gupta',
        'duration': '8 hours',
        'level': 'Beginner to Intermediate',
        'description': 'Master digital communication strategies for political campaigns, including social media management, content creation, and online community building.',
        'image': 'digital-communication.jpg',
        'topics': [
            'Social Media Strategy for Political Campaigns',
            'Content Creation & Management',
            'Digital Advertising & Targeting',
            'Crisis Communication in Digital Space',
            'Building Online Communities & Engagement'
        ],
        'demo_video': 'digital-communication-demo.mp4',
        'what_you_learn': [
            'Develop platform-specific social media strategies',
            'Create compelling political content for digital channels',
            'Plan and execute digital advertising campaigns',
            'Manage online reputation and crisis response',
            'Build and engage online supporter communities'
        ]
    },
    'campaign-tech': {
        'id': 'campaign-tech',
        'title': 'Campaign Technology & Tools',
        'category': 'Data & Technology',
        'price': 5999,
        'instructor': 'Vikram Singh',
        'duration': '10 hours',
        'level': 'Intermediate',
        'description': 'Explore and master the essential technology tools and platforms used in modern political campaigns, from CRM systems to analytics platforms.',
        'image': 'campaign-tech.jpg',
        'topics': [
            'Campaign CRM Systems & Implementation',
            'Mobile Apps for Field Operations',
            'Data Integration & Management',
            'Technology for Voter Outreach',
            'Security & Privacy Best Practices'
        ],
        'demo_video': 'campaign-tech-demo.mp4',
        'what_you_learn': [
            'Select and implement appropriate campaign technology stack',
            'Integrate data across multiple campaign systems',
            'Deploy mobile solutions for field teams',
            'Ensure data security and privacy compliance',
            'Optimize technology use for campaign objectives'
        ]
    },
    'political-consulting': {
        'id': 'political-consulting',
        'title': 'Professional Political Consulting',
        'category': 'Campaign Management',
        'price': 9999,
        'instructor': 'Aditya Khanna',
        'duration': '20 hours',
        'level': 'Advanced',
        'description': 'Comprehensive training for aspiring political consultants, covering campaign strategy, management, messaging, and all aspects of professional consulting services.',
        'image': 'political-consulting.jpg',
        'topics': [
            'Campaign Strategy Development',
            'Client Management & Relations',
            'Integrated Campaign Planning',
            'Budget Management & Resource Allocation',
            'Political Consulting as a Profession'
        ],
        'demo_video': 'political-consulting-demo.mp4',
        'what_you_learn': [
            'Develop comprehensive campaign strategies',
            'Manage client relationships effectively',
            'Integrate various campaign elements into cohesive plans',
            'Create and manage campaign budgets',
            'Establish yourself as a professional political consultant'
        ]
    }
}

# Course categories for organizing the courses page
course_categories = {
    'Campaign Operations': ['field-operations'],
    'Research & Insights': ['political-research'],
    'Data & Technology': ['data-analytics', 'campaign-tech'],
    'Communication': ['digital-communication'],
    'Campaign Management': ['political-consulting']
}

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

@app.route('/courses')
def courses_page():
    return render_template('courses.html', courses=courses, categories=course_categories)

@app.route('/courses/<course_id>')
def course_detail(course_id):
    course = courses.get(course_id)
    if not course:
        flash('Course not found.', 'danger')
        return redirect(url_for('courses_page'))
    
    return render_template('course_detail.html', course=course)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    cart_courses = []
    total = 0
    
    for item_id in cart_items:
        course = courses.get(item_id)
        if course:
            cart_courses.append(course)
            total += course['price']
    
    return render_template('cart.html', cart_items=cart_courses, total=total)

@app.route('/add-to-cart/<course_id>')
def add_to_cart(course_id):
    if course_id not in courses:
        flash('Course not found.', 'danger')
        return redirect(url_for('courses_page'))
    
    if 'cart' not in session:
        session['cart'] = []
    
    if course_id not in session['cart']:
        session['cart'].append(course_id)
        session.modified = True
        flash(f"Added {courses[course_id]['title']} to your cart.", 'success')
    else:
        flash('This course is already in your cart.', 'info')
    
    return redirect(url_for('cart'))

@app.route('/remove-from-cart/<course_id>')
def remove_from_cart(course_id):
    if 'cart' in session and course_id in session['cart']:
        session['cart'].remove(course_id)
        session.modified = True
        flash('Course removed from cart.', 'success')
    
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    cart_items = session.get('cart', [])
    if not cart_items:
        flash('Your cart is empty.', 'info')
        return redirect(url_for('courses_page'))
    
    cart_courses = []
    total = 0
    
    for item_id in cart_items:
        course = courses.get(item_id)
        if course:
            cart_courses.append(course)
            total += course['price']
    
    # In a real application, we would integrate with Stripe here
    
    return render_template('checkout.html', cart_items=cart_courses, total=total)

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    # This would be implemented with Stripe in a real application
    # For now, we'll simulate a successful purchase
    
    flash('Your purchase was successful! Check your email for access instructions.', 'success')
    session['cart'] = []  # Clear the cart
    
    return redirect(url_for('courses_page'))

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
