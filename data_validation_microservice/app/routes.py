from flask import Blueprint, request, jsonify
from .models import ExampleModel
from .validation import validate_data
from . import db

validation_bp = Blueprint('validation', __name__)

@validation_bp.route('/add-data', methods=['POST'])
def add_data():
    data = request.json.get('data')
    
    # Validate data
    errors = validate_data(data)
    if errors:
        return jsonify({'errors': errors}), 400
    
    # Save to database
    new_entry = ExampleModel(data=data)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({'message': 'Data added successfully!'}), 201
