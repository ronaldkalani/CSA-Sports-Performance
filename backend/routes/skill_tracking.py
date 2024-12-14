from flask import Blueprint, request, jsonify
from backend.utils.skill_assessment import evaluate_skills

skill_tracking_routes = Blueprint('skill_tracking_routes', __name__)

@skill_tracking_routes.route('/track', methods=['POST'])
def track_skills():
    data = request.json
    athlete_id = data.get('athlete_id')
    skill_data = data.get('skills')  # Example: {"leadership": 8, "accountability": 7}
    
    # Evaluate skills and provide AI-driven insights
    insights = evaluate_skills(skill_data)
    
    # Save skill tracking data to the database
    # Example database call:
    # db.save_skill_data(athlete_id, skill_data, insights)
    
    return jsonify({
        'message': 'Skills tracked successfully',
        'insights': insights
    }), 200

@skill_tracking_routes.route('/progress/<athlete_id>', methods=['GET'])
def get_progress(athlete_id):
    # Retrieve skill progress history for the athlete
    progress_data = []  # Replace with database call
    return jsonify({
        'athlete_id': athlete_id,
        'progress_data': progress_data
    }), 200
 
