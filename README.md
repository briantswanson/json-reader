# **json-reader**

This microservice uses ZeroMQ to receive a json file that contains a python dictionary.
The service will then pull data from the dictionary and return a string, formatted for Jovanny's program.
The program will return the string to the client as a confirmation that the microservice worked.

To use this file, download the json-reader file.

## **How to programmatically request data:**

To request data, using ZeroMQ initiate a connection with socket 1111. The user may decide to change this socket number as they like.

An example dictionary is:

{
    "title": "Spiderman 2",
    "console": "Playstation 5",
    "release year": 2023,
    "game series": "Spiderman",
    "developer": "Insomniac",
    "transaction date": "02-05-2024",
    "Price": 69.99
}

Please make sure your dictionary contains "title", "transaction date" and "price" for json-reader to work correctly.

I have included a client.py file that contains this test dictionary to send to json-reader.

The example return string will be:
02-05-2024: "Spiderman 2" ———————$69.99

To request the microservice, use the following command with ZeroMQ:
socket.send([json_containing_python_dict])

## **How to programmatically receive data:**

The following default function from ZeroMQ will receive the string on socket 1111:

socket.recv()

The string will be received as a Byte_String, users will need to use the .decode() functioon within Python to convert the Byte_String to a Python String.
