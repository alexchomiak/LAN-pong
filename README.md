# Python Client - Server Pong Implementation on Rasperry Pi Local Network

This is our final project for CS362, and it is an implementation of a multiplayer
game of pong in which the controllers connect wirelessly using a local network set up by a center pi. The center pi also broadcasts updated coordinates to the clients
of the players positions, and sends the score wirelessed to a raspberry pi with a scoreboard hooked up as a segment display.

## Team Members

- Alex Chomiak
- Tyler Lyczak
- Jigar Patel
- Amratya Saraswat

## Setup Instructions (Server)

You must use python version 3.7 if on MacOS Catalina to run this project, otherwise any Python3.6 and above version should be fine. Make sure you have pygame installed by running the command:

```
  pip3 install pygame
```

Now make sure you are in the server directory and run the command:

```
  python3 index.py
```

## Setup Instructions (Client)

You must also use Python3 for the client.
You can connect to the server by running this command in the Client directory:

```
  python3 client.py <port> <ip>
```

If no ip is provided, it will default to localhost.
