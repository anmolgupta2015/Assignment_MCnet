from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  #  Enables CORS for frontend requests

LHE_FILE = "top.lhe"

def parse_lhe(file_path, max_events=5):
    """Parse LHE file and extract event data, limiting to max_events."""
    if not os.path.exists(file_path):
        return {"error": f"LHE file '{file_path}' not found!"}

    events = []
    try:
        with open(file_path, "r") as f:
            event = []
            inside_event = False

            for line in f:
                line = line.strip()
                if "<event>" in line:
                    inside_event = True
                    event = []
                    continue
                elif "</event>" in line:
                    inside_event = False
                    if event:
                        events.append(event)
                   
                   
                    continue

                if inside_event:
                    parts = line.split()
                    if len(parts) < 10:
                        continue  # Skip malformed lines

                    status = int(parts[1])  # Particle status
                    if status != 1: 
                        continue

                    particle = {
                        "id": int(parts[0]),  # PDG ID
                        "px": float(parts[6]),
                        "py": float(parts[7]),
                        "pz": float(parts[8]),
                        "E": float(parts[9])
                    }
                    event.append(particle)

        return events if events else {"error": "No valid events found!"}
    
    except Exception as e:
        return {"error": f"Error parsing LHE file: {str(e)}"}

@app.route('/event', methods=['GET'])
def get_event():
    """Serve the first 5 parsed LHE events as JSON."""
    event_data = parse_lhe(LHE_FILE)
    #print(event_data) 
    return jsonify(event_data)  

if __name__ == '__main__':
    app.run(debug=True, port=5000)
