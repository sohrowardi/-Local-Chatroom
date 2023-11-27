# app.py
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    # Get the IP address
    ip_address = request.remote_addr

    # Format the message with IP address and device name
    formatted_msg = f"{ip_address} : {msg}"

    # Broadcast the formatted message to all connected clients
    emit('message', formatted_msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
