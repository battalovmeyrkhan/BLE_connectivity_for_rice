from pibody import Climate, Distance

print("[TELEMETRY] init...")

try:
    climate = Climate("A")
    print("[OK] Climate ready")
except Exception as e:
    print("[ERR] Climate init:", e)
    climate = None

try:
    distance = Distance("B")
    print("[OK] Distance ready")
except Exception as e:
    print("[ERR] Distance init:", e)
    distance = None


telemetry_data = {
    "temp": 0,
    "humidity": 0,
    "distance": 0
}


def update_telemetry():
    global telemetry_data

    try:
        if climate is not None:
            telemetry_data["temp"] = round(climate.read_temperature(), 1)
            telemetry_data["humidity"] = round(climate.read_humidity(), 1)
    except Exception as e:
        print("[ERR] Climate read:", e)

    try:
        if distance is not None:
            telemetry_data["distance"] = distance.read()
    except Exception as e:
        print("[ERR] Distance read:", e)

    print("[TELEMETRY]", telemetry_data)
    return telemetry_data
