from flask import Flask, request, jsonify
from parsers.spacy_pipeline import parse_text
from rules_engine import evaluate_rules
import uuid, time, json, os

app = Flask(__name__)
LOG_PATH = '/workspaces/repo-root/logs/requests.log'

def append_log(entry):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, 'a') as f:
        f.write(json.dumps(entry) + "\n")

@app.route('/api/nlp', methods=['POST'])
def nlp():
    payload = request.json
    text = payload.get('text','')
    parsed, confidence = parse_text(text)  # returns dict, float
    # rules engine returns primary + backups (mock for now)
    scenarios = evaluate_rules(parsed)
    req_id = str(uuid.uuid4())
    log_entry = {
        "id": req_id,
        "timestamp": time.time(),
        "text": text,
        "parsed": parsed,
        "confidence": confidence,
        "scenarios": scenarios
    }
    append_log(log_entry)
    return jsonify({"request_id": req_id, "parsed": parsed, "confidence": confidence, "scenarios": scenarios})
