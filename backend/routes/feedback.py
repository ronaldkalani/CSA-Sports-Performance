from flask import Blueprint, request, jsonify
from backend.utils.ai_analysis import analyze_feedback

feedback_routes = Blueprint('feedback_routes', __name__)

@feedback_routes.route('/submit', methods=['POST'])
def submit_feedback():
    data = request.json
    athlete_id = data.get('athlete_id')
    feedback_text = data.get('feedback')
    
    # Analyze the feedback using AI-driven models
    analysis = analyze_feedback(feedback_text)
    
    # Save feedback and insights to the database
    # Example database call:
    # db.save_feedback(athlete_id, feedback_text, analysis)
    
    return jsonify({
        'message': 'Feedback submitted successfully',
        'analysis': analysis
    }), 200

@feedback_routes.route('/get/<athlete_id>', methods=['GET'])
def get_feedback(athlete_id):
    # Retrieve feedback history for the athlete
    feedback_history = []  # Replace with database call
    return jsonify({
        'athlete_id': athlete_id,
        'feedback_history': feedback_history
    }), 200
 
