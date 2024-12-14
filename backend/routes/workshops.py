from flask import Blueprint, request, jsonify
from backend.utils.workshop_management import recommend_workshops

workshops_routes = Blueprint('workshops_routes', __name__)

@workshops_routes.route('/schedule', methods=['POST'])
def schedule_workshop():
    data = request.json
    workshop_details = data.get('details')  # Example: {"topic": "Leadership", "date": "2024-12-20"}
    
    # Save workshop details to the database
    # Example database call:
    # db.schedule_workshop(workshop_details)
    
    return jsonify({
        'message': 'Workshop scheduled successfully'
    }), 200

@workshops_routes.route('/recommend/<athlete_id>', methods=['GET'])
def recommend_workshop(athlete_id):
    # Generate personalized workshop recommendations
    recommendations = recommend_workshops(athlete_id)
    
    return jsonify({
        'athlete_id': athlete_id,
        'recommendations': recommendations
    }), 200

@workshops_routes.route('/feedback', methods=['POST'])
def workshop_feedback():
    data = request.json
    workshop_id = data.get('workshop_id')
    feedback = data.get('feedback')
    
    # Analyze workshop feedback
    # Example database call:
    # db.save_workshop_feedback(workshop_id, feedback)
    
    return jsonify({
        'message': 'Workshop feedback submitted successfully'
    }), 200
 
