from flask import Flask, render_template, request, jsonify
import random, json
from database import get_bus_timing, get_fare, register_complaint

app = Flask(__name__)

# Load intents
with open("intents.json","r",encoding="utf-8-sig") as f:
    intents = json.load(f)["intents"]

def chatbot_response(user_input):
    user_input = user_input.lower()

    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:   # simple keyword match
                if intent["tag"] == "bus_timing":
                    return f"Next buses: {get_bus_timing('A', 'B')}"
                elif intent["tag"] == "fare_info":
                    return f"Fare: ₹{get_fare('A', 'B')}"
                elif intent["tag"] == "complaint":
                    return register_complaint("User123", "Lost ticket")
                else:
                    return random.choice(intent["responses"])

  #  return "Sorry, I didn’t understand that 🤔. Try asking about bus timings, fares, or routes."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
