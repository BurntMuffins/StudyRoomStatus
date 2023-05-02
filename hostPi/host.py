####################################################################
# An API that recieves information from the sensors in study rooms 
# and puts the information into a JSON file to be stored and used
# by the website.
####################################################################

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json, os.path

NUM_OF_SENSORS = 3

def load_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)
        
# Creates a file that would hold the information from the sensors
if not os.path.isfile('./data.json'):
    f = open("data.json", 'x')
    f.write("{}")
    f.close()


app = Flask(__name__)
cors = CORS(app)


#----- app routes -----#

#route to the html file for the webpage
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/check-room", methods=["POST"])
def checkRoom():
    print(request.data)
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


# Creates all of the objects holding the status of each room
data = load_data()
for i in range(1, NUM_OF_SENSORS + 1):
    data[f"study-room-status-{i}"] = {"occupied":False} # added a new room/updating it also

save_data(data)

if __name__ == "__main__":
    app.run(host="localhost", debug=True)