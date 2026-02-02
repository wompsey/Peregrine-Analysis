from pprint import pprint
def L3_tele(entry_data: dict) -> bool:
    return "Coral L3 (teleop)" in entry_data["name"]


def L4_tele(entry_data: dict) -> bool:
    return "Coral L4 (teleop)" in entry_data["name"]

def L2_tele(entry_data: dict) -> bool:
    return "Coral L2 (teleop)" in entry_data["name"]

def L1_tele(entry_data: dict) -> bool:
    return "Coral L1 (teleop)" in entry_data["name"]

def L1_auto(entry_data: dict) -> bool:
    return "Coral L1 (auto)" in entry_data["name"]

def L2_auto(entry_data: dict) -> bool:
    return "Coral L2 (auto)" in entry_data["name"]

def L3_auto(entry_data: dict) -> bool:
    return "Coral L3 (auto)" in entry_data["name"]

def L4_auto(entry_data: dict) -> bool:
    return "Coral L4 (auto)" in entry_data["name"]

def deep_atempt(entry_data: dict) -> bool:
    return "Deep Climb Attempt" in entry_data["name"]
COUNT_FUNCTIONS = [
    L1_auto,
    L2_auto,
    L3_auto,
    L4_auto,
    L1_tele,
    L2_tele,
    L3_tele,
    L4_tele,
    deep_atempt
    

]
COUNT_NAMES = [
    "Coral L1 (auto)",
    "Coral L2 (auto)",
    "Coral L3 (auto)",
    "Coral L4 (auto)",
    "Coral L1 (teleop)",
    "Coral L2 (teleop)",
    "Coral L3 (teleop)",
    "Coral L4 (teleop)",
    "Deep Climb Attempt"
]
