import zmq
import json

test_input = {
    "title": "Spiderman 2",
    "console": "Playstation 5",
    "release year": 2023,
    "game series": "Spiderman",
    "developer": "Insomniac",
    "transaction date": "02-05-2024",
    "Price": 69.99
}

json_dictionary = json.dumps(test_input, indent = 4)

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(("tcp://localhost:1111"))

while True:
    socket.send_json(json_dictionary)
    message = socket.recv().decode()
    print(message)
    break