import datetime

# Dummy bus schedule (can expand later)
bus_schedule = {
    ("A", "B"): ["10:30 AM", "11:00 AM", "11:30 AM"],
    ("A", "C"): ["10:15 AM", "10:45 AM", "11:15 AM"]
}

# Dummy fare info
fare_info = {
    ("A", "B"): 25,
    ("A", "C"): 40
}

# Complaint storage
complaints = []

def get_bus_timing(start, end):
    """Return available bus timings between two points"""
    return bus_schedule.get((start, end), ["No buses found"])

def get_fare(start, end):
    """Return fare info between two points"""
    return fare_info.get((start, end), "Fare not available")

def register_complaint(user, issue):
    """Register a complaint and save with timestamp"""
    complaint = {
        "user": user,
        "issue": issue,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    complaints.append(complaint)
    return "Your complaint has been registered ✅"
