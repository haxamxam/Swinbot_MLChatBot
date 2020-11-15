#importing the libraries and dependancies

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from main import chat


#Configure app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'jsbcfsbfjefebw237u3gdbdc'

#Initializig Fask- SocketIO
socketio = SocketIO(app)

#Routing and Returning html files
@app.route( '/' )
def hello():
  return render_template( 'swinbot.html' )

@app.route('/chatbox')
def hi():
  return render_template('chatbox.html')

@app.route( '/swinbot' )
def h():
  return render_template( 'swinbot.html' )

def messageRecived():
  print( 'message was received!!!' )

#Sending data to the server side events
@socketio.on( 'my eventes' )
def handle_my_custom_event1( json1 ):
  message = json1['message']
  #printing the message to the terminal
  print(message)
  answer=chat(message)
  json1['answer'] = answer
  json1['bot']='AI'
  print( 'recived my event: ' + str(json1 ))
  socketio.emit( 'my response', json1, callback=messageRecived )

#main is phython file we are running
if __name__ == '__main__':
  socketio.run( app )
