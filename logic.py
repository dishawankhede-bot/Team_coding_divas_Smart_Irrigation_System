import random
from collections import deque

# ── Data Structures ──────────────────────────────────────────
moisture_history = []          # List  – all readings
sensor_data = {                # Dict  – multi-sensor values
    "Sensor1": 50,
    "Sensor2": 50,
    "Sensor3": 50
}
recent_queue = deque(maxlen=5) # Queue – latest 5 readings
weather_list = ["Sunny", "Rainy", "Cloudy"]

# ── Mutable state ────────────────────────────────────────────
state = {
    "threshold": 40,
    "tank_level": 100,
    "weather_index": 0,
    "pump_status": "OFF"
}

# ── Core logic ───────────────────────────────────────────────
def generate_moisture():
    """Generate a new moisture reading, update all structures, return result dict."""
    moisture = random.randint(10, 80)
    weather  = weather_list[state["weather_index"]]

    # Update sensor dict with random values per sensor
    for key in sensor_data:
        sensor_data[key] = random.randint(10, 80)

    # Pump decision
    if moisture < state["threshold"]:
        pump = "ON"
        if state["tank_level"] > 0:
            state["tank_level"] = max(0, state["tank_level"] - 2)
    else:
        pump = "OFF"

    state["pump_status"] = pump

    # Store in list and queue
    moisture_history.append(moisture)
    recent_queue.append(moisture)

    alerts = build_alerts(moisture, pump)

    return {
        "moisture": moisture,
        "pump": pump,
        "tank": state["tank_level"],
        "weather": weather,
        "threshold": state["threshold"],
        "sensor_data": dict(sensor_data),
        "recent": list(recent_queue),
        "alerts": alerts,
        "explanation": build_explanation(moisture, pump)
    }

def build_alerts(moisture, pump):
    alerts = []
    if state["tank_level"] < 20:
        alerts.append("⚠️ Low Tank Level! Please refill.")
    if moisture < state["threshold"]:
        alerts.append(f"💧 Low Moisture ({moisture}%) — Pump activated.")
    if pump == "ON":
        alerts.append("🚿 Pump is currently running.")
    return alerts

def build_explanation(moisture, pump):
    return (
        f"Moisture = {moisture}% | Threshold = {state['threshold']}% | "
        f"Pump turned {pump} because moisture is "
        f"{'below' if pump == 'ON' else 'above or equal to'} the threshold."
    )

def get_statistics():
    if not moisture_history:
        return {"avg": 0, "min": 0, "max": 0, "count": 0}
    return {
        "avg": round(sum(moisture_history) / len(moisture_history), 1),
        "min": min(moisture_history),
        "max": max(moisture_history),
        "count": len(moisture_history)
    }

def refill_tank():
    state["tank_level"] = 100
    return {"tank": 100, "message": "Tank refilled to 100%"}

def change_weather():
    state["weather_index"] = (state["weather_index"] + 1) % len(weather_list)
    return {"weather": weather_list[state["weather_index"]]}

def set_threshold(value):
    state["threshold"] = int(value)
    return {"threshold": state["threshold"]}

def get_history_list():
    return moisture_history[-20:]
