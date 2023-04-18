from requests import get, post
from time import sleep
from flask import Flask, jsonify, request
import json

NUM_OF_SENSORS = 2
app = Flask(__name__)

def load_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)

@app.route("/check-room", methods=["POST"])
def checkRoom():
    roomToCheck = request.json["room"]
    try:
        return jsonify(load_data()[roomToCheck])
    except KeyError:
        return jsonify("Room doesn't exist.")

@app.route("/update-room", methods=["POST"])
def updateRoom():
    roomToUpdate = request.json["room"]
    status = request.json["status"]
    try:
        data = load_data()
        data[roomToUpdate]["occupied"] = status
        save_data(data)
        return jsonify(f"Successfully updated room {roomToUpdate}'s occupation status.")
    except KeyError:
        return jsonify("Failed to update room " + str(roomToUpdate))

# data = load_data()
# data["study-room-status-1"] = {"occupied":False} # added a new room/updating it also
# data["study-room-status-2"] = {"occupied":True}
# save_data(data)
# print(load_data()["study-room-status-2"]["occupied"])

app.run(host="138.47.145.71", debug=True)