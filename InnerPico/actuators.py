print("[ACTUATORS] init...")

actuator_state = {
    "COOLER": False,
    "HEATER": False,
    "WINDOW_1": False,
    "WINDOW_2": False,
    "DOOR": False,
    "LIGHT": False,
    "PUMP": False,
}

automation_state = {
    "COOLER": False,
    "HEATER": False,
    "WINDOWS": False,
    "DOOR": False,
    "LIGHT": False,
    "PUMP": False,
}


def cooler_on():
    actuator_state["COOLER"] = True

def cooler_off():
    actuator_state["COOLER"] = False

def heater_on():
    actuator_state["HEATER"] = True

def heater_off():
    actuator_state["HEATER"] = False

def pump_on():
    actuator_state["PUMP"] = True

def pump_off():
    actuator_state["PUMP"] = False

def window_1_open():
    actuator_state["WINDOW_1"] = True

def window_1_close():
    actuator_state["WINDOW_1"] = False

def window_2_open():
    actuator_state["WINDOW_2"] = True

def window_2_close():
    actuator_state["WINDOW_2"] = False

def all_windows_open():
    actuator_state["WINDOW_1"] = True
    actuator_state["WINDOW_2"] = True

def all_windows_close():
    actuator_state["WINDOW_1"] = False
    actuator_state["WINDOW_2"] = False

def door_open():
    actuator_state["DOOR"] = True

def door_close():
    actuator_state["DOOR"] = False

def light_on():
    actuator_state["LIGHT"] = True

def light_uv():
    actuator_state["LIGHT"] = True

def light_off():
    actuator_state["LIGHT"] = False

def automation_on():
    global automation_state
    automation_state = {
        "COOLER": True,
        "HEATER": True,
        "WINDOWS": True,
        "DOOR": True,
        "LIGHT": True,
        "PUMP": True,
    }
    return automation_state

def automation_off():
    global automation_state
    automation_state = {
        "COOLER": False,
        "HEATER": False,
        "WINDOWS": False,
        "DOOR": False,
        "LIGHT": False,
        "PUMP": False,
    }
    return automation_state
