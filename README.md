# Local Chatroom

## Overview

This simple chat application is built using Flask and Flask-SocketIO to enable real-time communication between clients. Users can access the chat interface through a web browser and exchange messages instantly.

## Features

- **Real-time Messaging:** Utilizes Socket.IO to enable real-time bidirectional communication between the server and connected clients.
- **IP Address Logging:** Captures the IP address of each client and includes it in the displayed messages for reference.
- **Broadcast Functionality:** Messages sent by one client are broadcasted to all connected clients, creating a shared chat experience.

## Prerequisites

Before running the application, ensure that you have the following installed:

- Python (version 3.6 or higher)
- Flask
- Flask-SocketIO

Install the required dependencies using the following command:

```bash
pip install Flask Flask-SocketIO

Clone the repository:
```bash
git clone https://github.com/sohrowardi/Local-Chatroom.git
cd chat-app

Run the application:
```bash
python app.py

Access the chat interface at http://localhost:5000.

How it Works
Server Initialization: Flask app creation and Socket.IO initialization.

Web Interface: Default route renders the chat interface.

Socket Event Handling: Handles incoming messages, includes sender's IP, and broadcasts to all clients.

Run the Application: If executed directly, the Socket.IO server runs on 0.0.0.0:5000.

Contributors
@sohrowardi