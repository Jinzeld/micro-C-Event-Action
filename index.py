from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for events (replace with a database in production)
events = []

# Endpoint to receive event data and respond with a success message
@app.route('/save_event', methods=['POST'])
def save_event():
    # Get JSON data from the request
    data = request.json

    # Validate required fields
    required_fields = ['name', 'description', 'location', 'date', 'time']
    for field in required_fields:
        if field not in data:
            return jsonify({"success": False, "error": f"{field} is required"}), 400

    # Log the event data (or save it to a database)
    event = {
        "title": data['name'],
        "description": data['description'],
        "location": data['location'],
        "event_date": data['date'],
        "event_time": data['time'],
        "created_at": datetime.now().isoformat()  # Add a timestamp
    }
    events.append(event)  # Add to in-memory storage (replace with database logic)

    # Log the event data (for debugging)
    print(f"Received event data: {event}")

    # Return a success response with the event data
    return jsonify({
        "success": True,
        "message": "Event data received and processed successfully.",
        "event": event
    }), 200


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