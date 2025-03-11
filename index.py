from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# In-memory storage for events (replace with a database in production)
events = []

# Helper function to find an event by ID
def find_event_by_id(event_id):
    for event in events:
        if event['event_id'] == event_id:
            return event
    return None

# Edit an event
@app.route('/edit_event/<int:event_id>', methods=['PUT'])
def edit_event(event_id):
    data = request.json

    # Validate required fields
    required_fields = ['title', 'event_date', 'event_time']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    # Find the event by ID
    event = find_event_by_id(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    # Update the event
    event['title'] = data['title']
    event['event_date'] = data['event_date']
    event['event_time'] = data['event_time']

    return jsonify({
        "success": True,
        "message": "Event updated successfully.",
        "event": event
    })

# Delete an event
@app.route('/delete_event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    # Find the event by ID
    event = find_event_by_id(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    # Remove the event from the list
    events.remove(event)

    return jsonify({
        "success": True,
        "message": "Event deleted successfully."
    })

# Root route to display a message
@app.route('/')
def home():
    return "Flask Microservice for Editing and Deleting Events is Running!"


if __name__ == '__main__':
    app.run(debug=True)