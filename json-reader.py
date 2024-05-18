# Brian Swanson
# CS 361, Spring 2024
# Project Group 6
# Microservice A for Jovanny Gochez

"""

This is a microservice that will use ZeroMQ to receive a json containing a dictionary object from Python.
The service will convert the dictionary into a string that will be returned on ZeroMQ.

Input Example:
{
    "title": "Spiderman 2",
    "console": "Playstation 5",
    "release year": 2023,
    "game series": "Spiderman",
    "developer": "Insomniac",
    "transaction date": "02-05-2024",
    "Price": 69.99
}

Output Example:

"date": "title" ———————$“price”
02052024: "Spiderman 2" ———————$69.99


"""

import zmq
import json


# ZeroMQ set up here, socket 1111 is used as an example.
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:1111")

print("microservice a is online")

# While Loop used here to keep the service online and listening for transmissions.
while True:
    message = socket.recv_json()
    print(f"received {message}")

    # load the received string as a json to enable dictionary functionality
    received_dict = json.loads(message)

    # Translating the dictionary items to a string
    return_string = str(received_dict.get("transaction date")) + ": " + str(received_dict.get("title")) + " ———————$" + str(received_dict.get("Price"))
    print(return_string)

    # returning the string over ZeroMQ
    socket.send_string(return_string)