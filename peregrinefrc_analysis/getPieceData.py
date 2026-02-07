
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

#Marcus functions 

def deep_atempt(entry_data: dict) -> bool:
    return "Deep Climb Attempt" in entry_data["name"]

def Algae_proc_auto(entry_data: dict) -> bool:
    return "Algae in Processor (auto)" in entry_data["name"]

def Algae_in_net_auto(entry_data: dict) -> bool:
    return "Algae in Net (auto)" in entry_data["name"]

def Algae_proc_tele(entry_data: dict) -> bool:
    return "Algae in Processor (teleop)" in entry_data["name"]

def Robot_died(entry_data: dict) -> bool:
    return "Robot Died" in entry_data["name"]

def Played_defense(entry_data: dict) -> bool:
    return "Played Defense" in entry_data["name"]

def Shallow_climb_atempt(entry_data: dict) -> bool:
    return "Shallow Climb Attempt" in entry_data["name"]

def Algae_in_net_tele(entry_data: dict) -> bool:
    return "Algae in Net (teleop)" in entry_data["name"]


COUNT_FUNCTIONS = [
    L1_auto,
    L2_auto,
    L3_auto,
    L4_auto,
    Algae_proc_auto,
    Algae_in_net_auto,
    L1_tele,
    L2_tele,
    L3_tele,
    L4_tele,
    Algae_proc_tele,
    Algae_in_net_tele,
    

]
COUNT_NAMES = [
    "Coral L1 (auto)",
    "Coral L2 (auto)",
    "Coral L3 (auto)",
    "Coral L4 (auto)",
    "Algae in Processor (auto)",
    "Algea in Net (auto)",
    "Coral L1 (teleop)",
    "Coral L2 (teleop)",
    "Coral L3 (teleop)",
    "Coral L4 (teleop)",
    "Algae in Processor (teleop)",
    "Algea in Net (teleop)",
]

COUNT_SCORE_NAMES = ["Coral L1 (auto)",
    "Coral L2 (auto)",
    "Coral L3 (auto)",
    "Coral L4 (auto)",
    "Algae in Processor (auto)",
    "Algea in Net (auto)",
    "Coral L1 (teleop)",
    "Coral L2 (teleop)",
    "Coral L3 (teleop)",
    "Coral L4 (teleop)",
    "Algae in Processor (teleop)",
    "Algea in Net (teleop)",
    "Auto Score",
    "Teleop Score",
    "Total Score",]
COUNT_STATES_FUNC = [
    Shallow_climb_atempt, 
    deep_atempt, 
    Played_defense, 
    Robot_died]

COUNT_STATES_NAMES = [
    "Shallow Climb Attempt",
    "deep_atempt",
    "Played Defense",
    "Robot Died"]
