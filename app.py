from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import logic
import database

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate")
def generate():
    data = logic.generate_moisture()
    try:
        database.save_moisture_reading(
            "Sensor1", data["moisture"], data["weather"],
            data["pump"], data["tank"]
        )
        database.log_message(data["explanation"])
    except Exception as e:
        print(f"DB warning: {e}")
    return jsonify(data)

@app.route("/history")
def history():
    try:
        rows = database.get_history()
    except Exception:
        rows = []
    return jsonify({
        "db_history": rows,
        "memory_history": logic.get_history_list()
    })

@app.route("/refill", methods=["POST"])
def refill():
    result = logic.refill_tank()
    try:
        database.log_message("Tank refilled to 100%")
    except Exception:
        pass
    return jsonify(result)

@app.route("/weather", methods=["POST"])
def weather():
    return jsonify(logic.change_weather())

@app.route("/threshold", methods=["POST"])
def threshold():
    value = request.json.get("value", 40)
    return jsonify(logic.set_threshold(value))

@app.route("/statistics")
def statistics():
    return jsonify(logic.get_statistics())

@app.route("/logs")
def logs():
    try:
        return jsonify(database.get_logs())
    except Exception:
        return jsonify([])

@app.route("/reset", methods=["POST"])
def reset():
    logic.moisture_history.clear()
    logic.recent_queue.clear()
    return jsonify({"status": "reset"})

if __name__ == "__main__":
    app.run(debug=True)
