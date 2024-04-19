# Local Chatroom

A lightweight chat application built with Flask and Flask-SocketIO for real-time communication.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```
pip install Flask Flask-SocketIO
```

## Usage
1. Clone the repository:
```
git clone https://github.com/sohrowardi/Local-Chatroom.git
```
```
cd Local-Chatroom
```

2. Run the application:
```
python app.py
```
3.Access the chat interface at http://localhost:5000.


### File Structure
```
Local-Chatroom
    ├── app.py
    ├── README.md
    └── templates
        └── index.html
```
### How It Works
app.py: This file contains the Flask application setup, routes, and SocketIO events for handling messages.
index.html: This file represents the frontend of the chat application, allowing users to send and receive messages in real-time.