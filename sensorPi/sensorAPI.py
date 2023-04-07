from flask import Flask, jsonify, request
import socket, json

HOSTNAME = f"{socket.gethostname()}.local"
PORT = 7583

app = Flask(__name__)

## ROUTES START ##

