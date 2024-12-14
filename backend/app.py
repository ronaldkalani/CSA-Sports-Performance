from flask import Flask, request, jsonify

# Create the Flask app with a specific name
flask_app = Flask("CSA Sports Performance Backend")

# In-memory data store (replace with a database for production)
workshops = []
skills = []
feedback = []

# ---------------------
# Workshops Endpoints
# ---------------------
@flask_app.route('/api/workshops', methods=['GET'])
def get_workshops():
    """Retrieve all workshops."""
    return jsonify({'workshops': workshops})

@flask_app.route('/api/workshops', methods=['POST'])
def add_workshop():
    """Add a new workshop."""
    data = request.json
    if not data or 'title' not in data or 'date' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    workshop = {
        'id': len(workshops) + 1,
        'title': data['title'],
        'description': data.get('description', ''),
        'date': data['date']
    }
    workshops.append(workshop)
    return jsonify({'message': 'Workshop added successfully', 'workshop': workshop}), 201

# ---------------------
# Skills Endpoints
# ---------------------
@flask_app.route('/api/skills', methods=['GET'])
def get_skills():
    """Retrieve all tracked skills."""
    return jsonify({'skills': skills})

@flask_app.route('/api/skills', methods=['POST'])
def add_skill():
    """Track a new skill."""
    data = request.json
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    skill = {
        'id': len(skills) + 1,
        'name': data['name'],
        'description': data['description'],
        'athletes': data.get('athletes', [])
    }
    skills.append(skill)
    return jsonify({'message': 'Skill added successfully', 'skill': skill}), 201

# ---------------------
# Feedback Endpoints
# ---------------------
@flask_app.route('/api/feedback', methods=['GET'])
def get_feedback():
    """Retrieve all feedback."""
    return jsonify({'feedback': feedback})

@flask_app.route('/api/feedback', methods=['POST'])
def add_feedback():
    """Submit feedback."""
    data = request.json
    if not data or 'athlete_id' not in data or 'comments' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    feedback_entry = {
        'id': len(feedback) + 1,
        'athlete_id': data['athlete_id'],
        'comments': data['comments'],
        'rating': data.get('rating', 0)
    }
    feedback.append(feedback_entry)
    return jsonify({'message': 'Feedback submitted successfully', 'feedback': feedback_entry}), 201

# ---------------------
# Health Check
# ---------------------
@flask_app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify the server is running."""
    return jsonify({'status': 'ok'}), 200

# ---------------------
# Main
# ---------------------
if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0', port=5000)
 
