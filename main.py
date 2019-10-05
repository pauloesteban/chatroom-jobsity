from flask import Flask, render_template
from flask_socketio import SocketIO

""" Flask is the framework for the web app.
Flask-SocketIO enable server-client communication.
Client can use official libraries, e.g., SocketJS.
"""

# Secret key to keep the client-side sessions secure.
# 24-byte was generated outside using os.urandom(24).
app = Flask(__name__)
app.config['SECRET_KEY'] = '\xe4\\}\xfa H\xb2s)i\x9e%\xe5b\x15\xb6x\xa4+\x84\x81\xbeN\x17'
socketio = SocketIO(app)

# Rendering from templates folder in homepage
@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('Message received.')

# Custom event names 
@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)